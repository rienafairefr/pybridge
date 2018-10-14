import functools
import json
from contextlib import contextmanager
from datetime import datetime, timedelta

import dateutil.parser
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pybridge.database import get_one_or_create
from pybridge.models import Base, SyncTime
from pybridge.schemas import User, UserAccess, Account, LoanDetails, UserSchema, TransactionSchema
from pybridge.schemas import Bank, BankForm, SavingsDetails, Item, Transaction
from pybridge.utils import copy_dict

rooturl = 'https://sync.bankin.com'

url_authenticate = rooturl + '/v2/authenticate'
url_users = rooturl + '/v2/users'
url_accounts = rooturl + '/v2/accounts'

url_banks = rooturl + '/v2/banks'
url_bank_details = url_banks + '/'

url_items = rooturl + '/v2/items'
url_item = url_items + '/%i'
url_item_refresh = url_item + '/refresh'
url_transactions = rooturl + '/v2/transactions'
url_transactions_updated = rooturl + '/v2/transactions/updated'

url_redirect = url_items + '/connect?bank_id=%s&client_id=%s&access_token=%s'

version_headers = {'Bankin-Version': '2016-01-18'}

datetime_format = '%Y-%m-%dT%H:%M:%S.%fZ'


class BridgeConfig(object):
    def __init__(self, id, secret):
        self.id = id
        self.secret = secret


class BridgeUserCredentials(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password


def authenticated(f):
    @functools.wraps(f)
    def modified(self, session, usercredential, *args, **kwargs):
        user = session.query(User).get(usercredential.email)
        if user is None or user.credential.is_expired:
            user = self.authenticate_user(usercredential)
        return f(usercredential, *args, **kwargs)

    return modified


class BridgeClient(object):
    def __init__(self, config):
        self.config = config
        engine = create_engine('sqlite://')
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(engine)

    def dorequest(self, url, func, params=None, headers=None):
        if params is None:
            params = {}
        if headers is None:
            headers = {}
        client_dict = dict(client_id=self.config.id, client_secret=self.config.secret)

        returnvalue = func(url,
                           params=copy_dict(client_dict, params),
                           headers=copy_dict(version_headers, headers))
        if returnvalue.ok:
            return returnvalue
        else:
            raise Exception(returnvalue.text)

    @contextmanager
    def session_scope(self):
        """Provide a transactional scope around a series of operations."""
        session = self.Session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()


    def dorequest_authenticated(self, session, usercredential, url, func, params=None, headers=None):
        if params is None:
            params = {}
        if headers is None:
            headers = {}
        bankinuser = session.query(User).filter_by(email=usercredential.email).first()

        returnvalue = self.dorequest(url, func, params,
                                     headers=copy_dict(headers,
                                                       {
                                                           'Authorization': 'Bearer ' + bankinuser.credential.access_token}))
        if returnvalue.ok:
            return returnvalue
        else:
            raise Exception(returnvalue.text)

    def is_email_taken(self, email):
        query_user = self.dorequest(url_users, requests.get, params=dict(email=email))
        if query_user.ok:
            if email not in (x['email'] for x in query_user.json()['resources']):
                return False
        return True

    def create_user(self, user_credential):
        create_user = self.dorequest(url_users, requests.post,
                                     params=dict(email=user_credential.email, password=user_credential.password))
        data = json.loads(create_user.text)
        if create_user.status_code == 201:
            user_result = data
        elif create_user.status_code == 409:
            user_result = data['user']
        else:
            return False

        with self.session_scope() as session:
            user = UserSchema().load(user_result, session).data
            session.add(user)
            return user

    def get_bank(self, id):
        return self.get_response(url_banks, requests.get)

    def get_banks(self):
        banks = self.get_response(url_banks, requests.get)
        for bank in banks:
            forms = []
            for form in bank['form']:
                forms.append(BankForm(**form))
            bank['form'] = []
            bank_obj = get_one_or_create(db.session, Bank, **bank)
            bank_obj.form = forms
            db.session.commit()

    def fetch(self, session, user, user_credential):
        items = self.get_response_authenticated(user_credential, url_items, requests.get)
        bankinuser_items = []
        for item in items:
            bank_id = item['bank']['id']
            bank = session.query(Bank).get(bank_id)
            item['bank'] = bank
            item['accounts'] = []
            item_obj = get_one_or_create(session, Item, **item)
            bankinuser_items.append(item_obj)
        user.items = bankinuser_items

        accounts = self.get_response_authenticated(user_credential, url_accounts, requests.get)
        for account_details in accounts:
            account_details['item'] = session.query(Item).get(account_details['item']['id'])
            bank_id = account_details['bank']['id']
            bank = session.query(Bank).get(bank_id)
            account_details['bank'] = bank
            account_details['updated_at'] = dateutil.parser.parse(account_details['updated_at'])
            if account_details['savings_details'] is not None:
                account_details['savings_details'] = SavingsDetails(**account_details['savings_details'])
            if account_details['loan_details'] is not None:
                account_details['loan_details'] = LoanDetails(**account_details['loan_details'])

            account_obj = get_one_or_create(session, Account, **account_details)
            if not account_obj in user.accounts:
                user.accounts.append(account_obj)
                account_details['item'].accounts.append(account_obj)

    def test_login_user(self, usercredential):
        try:
            authenticated_user = self.get_response(url_authenticate, requests.post, params=dict(
                email=usercredential.email,
                password=usercredential.password))
            return True
        except:
            return False

    def authenticate_user(self, user_credential):
        authenticated_user = self.get_response(url_authenticate, requests.post, params=dict(
            email=user_credential.email,
            password=user_credential.password))
        with self.session_scope() as session:
            user = get_one_or_create(session, User, email=user_credential.email)
            user.access = get_one_or_create(session, UserAccess,
                                            expires_at=dateutil.parser.parse(authenticated_user['expires_at']),
                                            access_token=authenticated_user['access_token'])
            # fetch all the data for this user
            self.fetch(session, user, user_credential)

            session.commit()

        return user

    def get_response_authenticated(self, usercredential, url, func, params=None):
        return self._get_response(functools.partial(self.dorequest_authenticated, usercredential=usercredential), url,
                                  func, params)

    def get_response(self, url, func, params=None):
        return self._get_response(self.dorequest, url, func, params)

    def refresh_item(self, usercredential, item):
        self.dorequest_authenticated(usercredential, url_item_refresh % item.id, requests.delete)

    def delete_item(self, usercredential, item):
        self.dorequest_authenticated(usercredential, url_item % item.id, requests.delete)

    def _get_response(self, func_request, url, func, params=None):
        if params is None:
            params = {}
        data = func_request(url=url, func=func, params=params)
        loaded = json.loads(data.text)
        if 'pagination' in loaded:
            pagination = loaded['pagination']
            if pagination['next_uri'] is not None:
                return loaded['resources'] + self._get_response(func_request, rooturl + pagination['next_uri'], func)
            else:
                return loaded['resources']
        else:
            return loaded

    def treat_transactions(self, dictionaries):
        transactions = []
        for d in dictionaries:
            d['account_id'] = d['account']['id']
            d.pop('account')
            d['category_id'] = d['category']['id']
            d['updated_at'] = datetime.strptime(d['updated_at'], datetime_format)
            d['date'] = datetime.strptime(d['date'], '%Y-%m-%d').date()
            d.pop('category')
            transaction = TransactionSchema.load(d).data
            print('transaction id :' + transaction.id)
            transactions.append(transaction)
        return transactions

    @authenticated
    def get_transactions(self, usercredential):
        return self.treat_transactions(self.get_response_authenticated(usercredential, url_transactions, requests.get))

    def get_formatted_time(self, since):
        return datetime.strftime(since, datetime_format)[:-4] + 'Z'

    @authenticated
    def get_transactions_updated(self, usercredential, since):
        return self.treat_transactions(
            self.get_response_authenticated(usercredential, url_transactions_updated, requests.get,
                                            params={'since': self.get_formatted_time(since), 'limit': 50}))

    @authenticated
    def get_accounts(self, usercredential):
        return self.get_user(usercredential).accounts

    def banks_query(self):
        return self.session.query(Bank).order_by(Bank.name.asc())

    @authenticated
    def listAllAccountsAndAlertsAndTransactions(usercredential):
        listurl = rooturl + 'requests/listAllAccountsAndAlertsAndTransactions'
        result2 = request.post(listurl)
        return json.loads(result2.text)

    @authenticated
    def listBefore(usercredential, indate):
        listurlbefore = rooturl + 'transactions/listBefore'
        # query with Year-Month,
        result2 = db.session.post(listurlbefore, data={'year': indate.year, 'month': indate.month})
        print('query %s-%s' % (indate.year, indate.month))
        result_data = json.loads(result2.text)
        return result_data

    def delete_users(self):
        return self.dorequest(url_users, requests.delete)

    def get_clients(self):
        return self.dorequest(url_users, requests.get)
