from .expressions import BinaryExpression, JoinColumnExpression
from typing  import Optional

class ColumnAttribute:
    def __init__(self, column_type:str,
                        primary_key: Optional[bool] = False, 
                        not_null: Optional[bool] = False,
                        column_name: Optional[str] = None):
        self.table          = None
        self.primary_key    = primary_key
        self.column_type    = column_type
        self.not_null       = not_null
        self.column_name    = column_name


    def __repr__(self):
        return f"<ColumnAttribute: Column Name:{self.column_name} Column Type:{self.column_type} Primary_key:{self.primary_key} Not Null:{self.not_null}>"
        pass


    def __get__(self, instance, owner):
        return self

    def __eq__(self, other):
        if isinstance(other, ColumnAttribute):
            return BinaryExpression(left=JoinColumnExpression(self.table, self.column_name), 
                                    Predicates='=', 
                                    right=JoinColumnExpression(other.table, other.column_name))
        return BinaryExpression(left=self.column_name, Predicates='=', right=other)

    def __gt__(self, other):
        if isinstance(other, ColumnAttribute):
            return BinaryExpression(left=JoinColumnExpression(self.table, self.column_name), 
                                    Predicates='>', 
                                    right=JoinColumnExpression(other.table, other.column_name))
        return BinaryExpression(left=self.column_name, Predicates='>', right=other)
    def __ge__(self,other):
        if isinstance(other, ColumnAttribute):
            return BinaryExpression(left=JoinColumnExpression(self.table, self.column_name), 
                                    Predicates='>=', 
                                    right=JoinColumnExpression(other.table, other.column_name))
        return BinaryExpression(left=self.column_name, Predicates='>=', right=other)
    
    def __lt__(self,other):
        if isinstance(other, ColumnAttribute):
            return BinaryExpression(left=JoinColumnExpression(self.table, self.column_name), 
                                    Predicates='<', 
                                    right=JoinColumnExpression(other.table, other.column_name))
        return BinaryExpression(left=self.column_name, Predicates='<', right=other)
    def __le__(self,other):
        if isinstance(other, ColumnAttribute):
            return BinaryExpression(left=JoinColumnExpression(self.table, self.column_name), 
                                    Predicates='<=', 
                                    right=JoinColumnExpression(other.table, other.column_name))
        return BinaryExpression(left=self.column_name, Predicates='<=', right=other)
    
    def __ne__ (self,other):
        if isinstance(other, ColumnAttribute):
            return BinaryExpression(left=JoinColumnExpression(self.table, self.column_name), 
                                    Predicates='<>', 
                                    right=JoinColumnExpression(other.table, other.column_name))
        return BinaryExpression(left=self.column_name, Predicates='<>', right=other)
    