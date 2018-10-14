from sqlalchemy import types, Column, String


class ResourceMixin(object):
    resource_type = Column(String)
    resource_uri = Column(String)