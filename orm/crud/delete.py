from ..builder.sql import DeleteObject
from ..declarative.base import TableModel
from ..builder.expressions import BinaryExpression
from ..builder.clauses import WhereClause, AndClause, OrClause


class Delete:

    def __init__(self, table:TableModel, conn):
        self.sql = DeleteObject(table)
        self.conn = conn
        pass

    def filter(self, *args):
        for filter in args:
            if isinstance(filter,BinaryExpression):
                self.sql.where_clauses.append(WhereClause(filter))
            elif isinstance(filter,(AndClause, OrClause)):
                self.sql.where_clauses.append(filter.clauses)
            else:
                raise ValueError(f'Tipo {type(filter)} não é valido, requerido o tipo {type(BinaryExpression)}')
        return self
    

    def __repr__(self):
        string  = f" <Delete: TableName: {self.sql.main_table.__tablename__} \n"
        string += f" filter: {self.sql.where_clauses}\n"
        string += f">"
        return string