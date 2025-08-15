from ..builder.sql import InsertObject
from ..declarative.base import TableModel


class Insert:

    def __init__(self, table:TableModel, conn):
        self.sql = InsertObject(table)
        self.conn = conn
        pass
    
    def values(self, **kargs):
        for k, v in kargs.items():
            self.sql.columns.append(k)
            self.sql.value.append(v)    
            ...
        ...

        return self
    

    def __repr__(self):
        string  = f" <Insert: TableName: {self.sql.main_table.__tablename__} \n"
        string += f" columns: {self.sql.columns} \n"
        string += f" values: {self.sql.value}\n"
        string += f">"
        return string
