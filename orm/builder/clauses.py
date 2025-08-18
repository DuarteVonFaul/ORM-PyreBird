from .operators import OperatorEnum, JoinTypeEnum
from .expressions import BinaryExpression

class WhereClause:
    def __init__(self, binary:BinaryExpression, operator:OperatorEnum = OperatorEnum.AND):
        self.operator = operator
        self.binary = binary
    def __repr__(self):
        return f"<WhereClause: Operator:{self.operator.value} {self.binary}>"

class JoinClause:
    def __init__(self, table_to_join: str, join_type:JoinTypeEnum = JoinTypeEnum.INNER):
        self.table_to_join = table_to_join 
        self.join_type = join_type         
        
        self.on_conditions = []

    def add_on_condition(self, binary:BinaryExpression):
        self.on_conditions.append(binary)
        return self
    
    def __repr__(self):
        return f"<JoinClause: {self.join_type} {self.table_to_join.__tablename__} \nConditions: {self.on_conditions}>"
    
class AndClause:
    def __init__(self, clauses):
        self.clauses = clauses
    
    def __repr__(self):
        return f"<AndClause: {self.clauses}>"

class OrClause:
    def __init__(self, clauses):
        self.clauses = clauses
    
    def __repr__(self):
        return f"<OrClause: {self.clauses}>"


