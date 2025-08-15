from ..builder.sql import SelectObject
from ..declarative.base import TableModel
from ..builder.expressions import BinaryExpression,JoinColumnExpression
from ..builder.clauses import WhereClause, JoinClause 

from typing import Optional

class Select:


    def __init__(self, table:TableModel, conn, limit:Optional[int] = None):

        self.sql = SelectObject(table)
        if(limit):
            self.sql.limit = limit

        ...

    
    def columns_to_select(self, *args):

        self.sql.columns_to_select = args

        return self
        ...
    
    def filter(self, filters:list[BinaryExpression]):
        for filter in filters:
            if isinstance(filter,BinaryExpression):
                self.sql.where_clauses.append(WhereClause(filter))
            else:
                raise ValueError(f'Tipo {type(filter)} não é valido, requerido o tipo {type(BinaryExpression)}')
        
        return self
        
        ...
    
    def join(self, table:TableModel,joins:list[BinaryExpression]):
        clause = JoinClause(table)
        for join in joins:
            if isinstance(join,BinaryExpression):
                if(isinstance(join.left,JoinColumnExpression) and isinstance(join.right,JoinColumnExpression)):
                    clause.add_on_condition(join)
                else:
                  raise ValueError(f'Tipo {type(join.left)} não é valido, requerido o tipo {type(JoinColumnExpression)}')  
            else:
                raise ValueError(f'Tipo {type(join)} não é valido, requerido o tipo {type(BinaryExpression)}')
        self.sql.joins.append(clause)
        
        return self
        ...
    
    def orden_by(self, *args):
        self.orden_by = args

        return self
        ...

    def __repr__(self):
        string  = f" <Select: TableName: {self.sql.main_table.__tablename__} \n"
        string += f" limit: {self.sql.limit} \n"
        string += f" Columns: {self.sql.columns_to_select}\n"
        string += f" filter: {self.sql.where_clauses}\n"
        string += f" join: {self.sql.joins}\n"
        string += f" orden_by: {self.sql.order_by}"
        string += f">"
        return  string
        
        pass
    ...