from marshmallow import Schema, fields
from marshmallow_sqlalchemy import field_for, ModelSchema

from pybridge.models import User, UserAccess, Account, LoanDetails, SavingsDetails, Item, Category, Transaction, Bank
from pybridge.models.banks import BankForm


class DecimalInteger(fields.Field):
    def _serialize(self, value, attr, obj):
        if value is None:
            return None
        return int(value * 100)

    def _deserialize(self, value, attr, obj):
        if value is None:
            return None
        return float(value) / 100


class UserSchema(ModelSchema):

    class Meta:
        model = User


class CredentialSchema(Schema):
    class Meta:
        model = UserAccess


class AccountSchema(Schema):
    class Meta:
        model = Account

    balance = DecimalInteger()


class LoanDetailsSchema(Schema):
    class Meta:
        model = LoanDetails

    borrowed_capital = DecimalInteger()
    repaid_capital = DecimalInteger()
    remaining_capital = DecimalInteger()


class SavingsDetailsSchema(Schema):
    class Meta:
        model = SavingsDetails


class ItemSchema(Schema):
    class Meta:
        model = Item


class CategorySchema(Schema):
    class Meta:
        model = Category


class TransactionSchema(Schema):
    class Meta:
        model = Transaction


class BankFormSchem(Schema):
    class Meta:
        model = BankForm


class BankSchema(Schema):
    class Meta:
        model = Bank
