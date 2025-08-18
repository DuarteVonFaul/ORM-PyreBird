from ..builder.sql import UpdateObject
from ..declarative.base import TableModel
from ..builder.expressions import BinaryExpression
from ..builder.clauses import WhereClause


class Update:

    def __init__(self, table:TableModel, conn):
        self.sql = UpdateObject(table)
        self.conn = conn
        pass
    
    def Set(self, **kargs):
        for k, v in kargs.items():
            self.sql.columns.append(k)
            self.sql.set.append(v)    
            ...
        ...

        return self

    def filter(self, *args):
        for filter in args:
            if isinstance(filter,BinaryExpression):
                self.sql.where_clauses.append(WhereClause(filter))
            else:
                raise ValueError(f'Tipo {type(filter)} não é valido, requerido o tipo {type(BinaryExpression)}')
        
        return self
    

    def __repr__(self):
        string  = f" <Update: TableName: {self.sql.main_table.__tablename__} \n"
        string += f" columns: {self.sql.columns} \n"
        string += f" set: {self.sql.set}\n"
        string += f" filter: {self.sql.where_clauses}\n"
        string += f">"
        return string