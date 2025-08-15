from .operators import OperatorEnum, JoinTypeEnum
from .expressions import BinaryExpression

class WhereClause:
    def __init__(self, binary:BinaryExpression):
        self.operator = OperatorEnum.AND
        self.binary = binary
    def __repr__(self):
        return f"<WhereClause: {self.binary}>"

class JoinClause:
    def __init__(self, table_to_join: str):
        self.table_to_join = table_to_join 
        self.join_type = JoinTypeEnum.INNER         
        
        self.on_conditions = []

    def add_on_condition(self, binary:BinaryExpression):
        self.on_conditions.append(binary)
        return self
    
    def __repr__(self):
        return f"<JoinClause: {self.join_type} {self.table_to_join.__tablename__} Conditions: {self.on_conditions}>"