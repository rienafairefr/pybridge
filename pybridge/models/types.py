from sqlalchemy import types, Column, String


class DecimalInteger(types.TypeDecorator):
    impl = types.Integer

    def load_dialect_impl(self, dialect):
        return dialect.type_descriptor(types.Integer)

    def process_bind_param(self, value, dialect):
        return int(value * 100) if value is not None else None

    def process_result_value(self, value, dialect):
        return float(value) / 100 if value is not None else None


class ResourceMixin(object):
    resource_type = Column(String)
    resource_uri = Column(String)