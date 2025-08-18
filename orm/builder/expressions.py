
class BinaryExpression:
    def __init__(self, left, Predicates, right):
        self.left = left
        self.predicates = Predicates
        self.right = right
        pass
    
    def __repr__(self):
        return f"<BinaryExpression: {self.left} {self.predicates} {self.right}>"


class ColumnExpression:
    def __init__(self, table, column):
        self.table = table
        self.column = column
        pass
    def __repr__(self):
        return f"<ColumnExpression: {self.table}.{self.column}>"
    
    

class RelationShipExpression:

    def __init__(self, related_column, table, referent_column, type):
        self.related_column = related_column 
        self.table          = table
        self.referent_column= referent_column
        self.type           = type
        pass