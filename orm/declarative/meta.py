from ..builder.attributes import ColumnAttribute

class TableDeclarativeMeta(type):

    def __new__(cls,name,bases,namespace):

        tablename = None
        columns = []
        if(not namespace.get('__tablename__')):
            tablename = namespace.get('__name__', name.lower())
            ...
        else:
            tablename = namespace.get('__tablename__', name.lower())
        namespace['__tablename__'] = tablename

        for attr_name, attr_value in namespace.items():
             if isinstance(attr_value, ColumnAttribute):
                if not attr_value.column_name:
                    attr_value.column_name = attr_name
                attr_value.table = tablename
                columns.append(attr_value)
        namespace['__columns__'] = columns
        return super().__new__(cls,name,bases,namespace)
    
    def __repr__(self):
        return f"<TableModel: Name {self.__tablename__} Columns {self.__columns__} "
    
