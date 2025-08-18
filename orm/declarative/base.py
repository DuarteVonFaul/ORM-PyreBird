from .meta import TableDeclarativeMeta
from orm.builder.attributes import ColumnAttribute

class TableModel(metaclass=TableDeclarativeMeta):   
    
    ...


def column( type_, primary_key=False, not_null=False, unique=False, default=None, column_name=None):
    return ColumnAttribute( type_, primary_key=primary_key, not_null=not_null, column_name=column_name)