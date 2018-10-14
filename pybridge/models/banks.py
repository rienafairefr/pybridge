from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from pybridge.pybridge.models import Base
from pybridge.pybridge.models.types import ResourceMixin


class Bank(Base, ResourceMixin):
    __tablename__ = 'bridge_banks'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    country_code = Column(String)
    automatic_refresh = Column(Boolean, name='automatic_refresh_bool')


class BankForm(Base):
    __tablename__ = 'bridge_bankforms'
    id = Column(Integer, primary_key=True)

    bank_id = Column(ForeignKey('bridge_banks.id'), nullable=True)
    bank = relationship('Bank', backref='form')

    label = Column(String)
    isNum = Column(String)
    type = Column(String)
    maxLength = Column(Integer, nullable=True)