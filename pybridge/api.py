import hashlib
from datetime import datetime, timedelta

import dateutil.parser
import functools
import requests
import json

from pybridge.database import get_one_or_create
from pybridge.models import User, Credential, Account, LoanDetails, SavingsDetails, Item, Transaction, SyncTime
from pybridge.models.banks import Bank, BankForm
from pybridge.utils import Bunch, copy_dict

requests.packages.urllib3.disable_warnings()

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


class BridgeClient(object):
    def __init__(self, config):
        self.config = config



    def dorequest(self, url, func, params=None, headers=None):
        if params is None:
            params = {}
        if headers is None:
            headers = {}
        client_dict = dict(client_id=self.config.BWS_ID, client_secret=self.config.BWS_KEY)

        returnvalue = func(url,
                           params=copy_dict(client_dict, params),
                           headers=copy_dict(version_headers, headers), verify=False)
        if returnvalue.ok:
            return returnvalue
        else:
            raise Exception(returnvalue.text)


    def dorequest_authenticated(self, session, usercredential, url, func, params=None, headers=None):
        if params is None:
            params = {}
        if headers is None:
            headers = {}
        bankinuser = session.query(User).filter_by(email=usercredential.email).first()

        returnvalue = self.dorequest(url, func, params,
                                headers=copy_dict(headers,
                                                  {'Authorization': 'Bearer ' + bankinuser.credential.access_token}))
        if returnvalue.ok:
            return returnvalue
        else:
            raise Exception(returnvalue.text)


    def is_email_taken(email):
        query_user = dorequest(url_users, requests.get, params=dict(email=email))
        if query_user.ok:
            if email not in (x['email'] for x in query_user.json()['resources']):
                return False
        return True


    def createuser(session, usercredential):
        create_user = dorequest(url_users, requests.post,
                                params=dict(email=usercredential.email,
                                            password=pw_from_username(usercredential.email)))
        data = json.loads(create_user.text)
        if create_user.status_code == 201:
            user_result = data
        elif create_user.status_code == 409:
            user_result = data['user']
        else:
            return False
        bankinuser = User(credential=Credential(), **user_result)
        session.add(bankinuser)
        session.commit()
        return True


    def refresh_banks():
        banks = get_response(url_banks, requests.get)
        for bank in banks:
            forms = []
            for form in bank['form']:
                forms.append(BankForm(**form))
            bank['form'] = []
            bank_obj = get_one_or_create(db.session, Bank, **bank)
            bank_obj.form = forms
            db.session.commit()


    def fetch(session, bankinuser, usercredential):
        items = get_response_authenticated(usercredential, url_items, requests.get)
        bankinuser_items = []
        for item in items:
            bank_id = item['bank']['id']
            bank = session.query(Bank).get(bank_id)
            item['bank'] = bank
            item['accounts'] = []
            item_obj = get_one_or_create(session, Item, **item)
            bankinuser_items.append(item_obj)
        bankinuser.items = bankinuser_items

        accounts = get_response_authenticated(usercredential, url_accounts, requests.get)
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

            account_obj = get_one_or_create(session,Account,**account_details)
            if not account_obj in bankinuser.accounts:
                bankinuser.accounts.append(account_obj)
                account_details['item'].accounts.append(account_obj)


    def pw_from_username(username):
        return hashlib.sha1(username.encode('utf-8')).hexdigest()


    def test_login_user(usercredential):
        try:
            authenticated_user = get_response(url_authenticate, requests.post, params=dict(
            email=usercredential.email,
            password=pw_from_username(usercredential.email)))
            return True
        except:
            return False


    def fetch_bankinuser(session, usercredential):
        authenticated_user = get_response(url_authenticate, requests.post, params=dict(
            email=usercredential.email,
            password=pw_from_username(usercredential.email)))

        bankinuser = get_one_or_create(session, User, email=usercredential.email)
        bankinuser.credential = get_one_or_create(session, Credential,
                                                  expires_at=dateutil.parser.parse(authenticated_user['expires_at']),
                                                  access_token=authenticated_user['access_token'])
        session.commit()
        # fetch all the data for this user
        fetch(bankinuser, usercredential)

        return bankinuser


    def authenticated(self, f):
        def modified(session, usercredential, *args, **kwargs):
            bankinuser = session.query(User).get(usercredential.email)
            if bankinuser is None or bankinuser.credential.is_expired:
                bankinuser = fetch_bankinuser(usercredential)
            return f(usercredential, *args, **kwargs)

        return modified


    def get_response_authenticated(usercredential, url, func, params=None):
        return _get_response(functools.partial(dorequest_authenticated, usercredential=usercredential), url, func, params)


    def get_response(url, func, params=None):
        return _get_response(dorequest, url, func, params)


    def get_items(usercredential):
        return get_user(usercredential).items


    def refresh_item(usercredential,item):
        dorequest_authenticated(usercredential, url_item_refresh % item.id, requests.delete)


    def delete_item(usercredential,item):
        dorequest_authenticated(usercredential, url_item % item.id, requests.delete)


    def get_user(session, usercredential=current_user):
        user = session.query(User).get(usercredential.email)
        if user is None or user.credential.is_expired():
            user = fetch_bankinuser(usercredential)
            session.add(user)

        if user.last_sync_time is None:
            sync_time = datetime.now()-timedelta(days=1)
            last_sync_time = datetime(year=sync_time.year,month=sync_time.month,day=sync_time.day)
            user.last_sync_time = SyncTime(time=last_sync_time)

        for item in user.items:
            if item is None:
                continue
            if item.accounts is None:
                continue
            for account in item.accounts:
                if item.status != 0:
                    account.name=item.status.inv_map[item.status]
                    break
                if not db.session.query(AccountMapping).filter_by(account=account).first():
                    map_obj = get_one_or_create(db.session, AccountMapping,
                                                user=user,
                                                account=account,
                                                remote_account_name=account.bank.name+":"+account.name)
                    if map_obj is not None:
                        user.maps.append(map_obj)
                    else:
                        pass

        db.session.commit()
        return user


    def logout_bankin_user(usercredential: UserCredential):
        url_logout = rooturl + '/v2/logout'
        dorequest_authenticated(usercredential, url_logout, requests.post)


    def _get_response(func_request, url, func, params=None):
        if params is None:
            params = {}
        data = func_request(url=url, func=func, params=params)
        loaded = json.loads(data.text)
        if 'pagination' in loaded:
            pagination = loaded['pagination']
            if pagination['next_uri'] is not None:
                return loaded['resources'] + _get_response(func_request,rooturl + pagination['next_uri'], func)
            else:
                return loaded['resources']
        else:
            return loaded

    datetime_format =  '%Y-%m-%dT%H:%M:%S.%fZ'


    def treat_transactions(dictionaries):
        transactions = []
        for d in dictionaries:
            d['account_id'] = d['account']['id']
            d.pop('account')
            d['category_id'] = d['category']['id']
            d['updated_at'] = datetime.strptime(d['updated_at'], datetime_format)
            d['date'] = datetime.strptime(d['date'], '%Y-%m-%d').date()
            d.pop('category')
            transaction = get_one_or_create(db.session,Transaction,**d)
            print('transaction id :'+transaction.id)
            transactions.append(transaction)
        return transactions


    @authenticated
    def get_transactions(usercredential):
        return treat_transactions(get_response_authenticated(usercredential,url_transactions,requests.get))


    def get_formatted_time(since):
        return datetime.strftime(since,datetime_format)[:-4]+'Z'


    @authenticated
    def get_transactions_updated(usercredential,since):
        return treat_transactions(get_response_authenticated(usercredential, url_transactions_updated, requests.get,
                                                             params = {'since':get_formatted_time(since), 'limit':50}))

    @authenticated
    def get_accounts(usercredential):
        return get_user(usercredential).accounts


    def banks_query():
        return db.session.query(Bank).order_by(Bank.name.asc())


    @authenticated
    def listAllAccountsAndAlertsAndTransactions(usercredential):
        listurl = rooturl + 'requests/listAllAccountsAndAlertsAndTransactions'
        result2 = db.session.post(listurl)
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
        self.dorequest(url_users, requests.delete)
