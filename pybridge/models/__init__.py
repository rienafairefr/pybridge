from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, DateTime, Date, Float
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from pybridge.pybridge.models import ResourceMixin, DecimalInteger, Bank
from pybridge.pybridge.models.banks import Bank
from pybridge.pybridge.models.types import ResourceMixin, DecimalInteger

Base = declarative_base()


class User(Base, ResourceMixin):
    __tablename__ = 'bridge_users'
    id = Column(Integer, primary_key=True)

    email = Column(ForeignKey('usercredentials.email'))
    uuid = Column(String)

    credential_id = Column(ForeignKey('bridge_credentials.id'))
    credential = relationship('Credential')

    _items = relationship('UserItems')
    items = association_proxy('_items', 'item', creator=lambda _i: UserItems(item=_i))

    _accounts = relationship('UserAccounts')
    accounts = association_proxy('_accounts', 'account', creator=lambda _i: UserAccounts(account=_i))

    last_sync_time = relationship('SyncTime', uselist=False, back_populates='user')
    fetched_elements_to_sync = Column(Boolean())

    hook_url = Column(String)

    maps = relationship('AccountMapping')

    def __str__(self):
        return 'Bankin User ' + self.email


class Credential(Base):
    __tablename__ = 'bridge_credentials'
    id = Column(Integer, primary_key=True)

    access_token = Column(String)
    expires_at = Column(DateTime)

    @property
    def is_expired(self):
        if self.expires_at is None or datetime.now() > self.expires_at:
            return True


class Account(Base, ResourceMixin):
    __tablename__ = 'bridge_accounts'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    balance = Column(DecimalInteger)
    currency_code = Column(String(3))
    status = Column(Integer)
    type = Column(String)
    updated_at = Column(DateTime)
    item_id = Column(ForeignKey('bridge_items.id'))
    item = relationship('Item', backref='accounts')
    bank_id = Column(ForeignKey('bridge_banks.id'))
    bank = relationship(Bank, backref='accounts')
    loan_details_id = Column(ForeignKey('bridge_loan_details.id'), nullable=True)
    loan_details = relationship('LoanDetails', backref='account')
    savings_details_id = Column(ForeignKey('bridge_savings_details.id'), nullable=True)
    savings_details = relationship('SavingsDetails', backref='account')


class LoanDetails(Base):
    __tablename__ = 'bridge_loan_details'
    id = Column(Integer, primary_key=True)

    next_payment_date = Column(Date)
    next_payment_amount = Column(Integer)
    maturity_date = Column(Date)
    opening_date = Column(Date)
    interest_rate = Column(Float)
    type = Column(String)
    borrowed_capital = Column(DecimalInteger)
    repaid_capital = Column(DecimalInteger)
    remaining_capital = Column(DecimalInteger)

# TODO unimplemented, stocks

class SavingsDetails(Base):
    __tablename__ = 'bridge_savings_details'
    id = Column(Integer, primary_key=True)


class Item(Base, ResourceMixin):
    __tablename__ = 'bridge_items'

    id = Column(Integer, primary_key=True)
    status = Column(Integer)
    bank_id = Column(ForeignKey('bridge_banks.id'))
    bank = relationship(Bank)

    _accounts = relationship('ItemAccounts')
    accounts = association_proxy('_accounts', 'account', creator=lambda _i: ItemAccounts(account=_i))


class Transaction(Base, ResourceMixin):
    __tablename__ = 'bridge_transactions'

    is_deleted = Column(Boolean, name='is_deleted_bool')
    updated_at = Column(DateTime)
    amount = Column(DecimalInteger)
    id = Column(Integer, primary_key=True)
    account_id = Column(ForeignKey('bridge_accounts.id'))
    account = relationship(Account)
    resource_uri = Column(String)
    date = Column(Date)
    raw_description = Column(String)
    currency_code = Column(String)

    category_id = Column(ForeignKey('bridge_categories.id'))
    category = relationship('Category')
    resource_type = Column(String)
    description = Column(String)


class Category(Base, ResourceMixin):
    __tablename__ = 'bridge_categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(ForeignKey('bridge_categories.id'))
    parent = relationship('Category')


class SyncTime(Base):
    __tablename__ = 'bankinsynctime'
    user_id = Column(ForeignKey('bankinusers.id'), primary_key=True)
    user = relationship('User', primaryjoin=user_id == User.id, back_populates='last_sync_time', uselist=False)
    time = Column(DateTime)

# linking tables

class UserItems(Base):
    __tablename__ = 'bridge_useritems'

    id = Column(Integer,primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey('bridge_users.id'))
    user = relationship('User', primaryjoin=user_id == User.id, cascade='all', single_parent=True)
    item_id = Column(ForeignKey('bridge_items.id'))
    item = relationship('Item', primaryjoin=item_id == Item.id, cascade='all', single_parent=True)


class UserAccounts(Base):
    __tablename__ = 'bridge_useraccounts'

    user_id = Column(ForeignKey('bridge_users.id'), primary_key=True)
    user = relationship('User', primaryjoin=user_id == User.id)
    account_id = Column(ForeignKey('bridge_accounts.id'), primary_key=True)
    account = relationship('Account', primaryjoin=account_id == Account.id)


class ItemAccounts(Base):
    __tablename__ = 'bridge_itemaccounts'

    item_id = Column(ForeignKey('bridge_initems.id'), primary_key=True)
    item = relationship('Item', primaryjoin=item_id == Item.id)
    account_id = Column(ForeignKey('bridge_accounts.id'), primary_key=True)
    account = relationship('Account', primaryjoin=account_id == Account.id)