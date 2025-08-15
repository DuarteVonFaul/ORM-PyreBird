class SelectObject:
    def __init__(self, main_table):
        self.main_table = main_table
        self.columns_to_select = []
        self.joins = [] 
        self.where_clauses = []
        self.order_by = []
        
        self.limit = None
        self.offset = None


class InsertObject:
    def __init__(self, main_table):
        self.main_table = main_table
        self.columns = []
        self.value = []
        pass
    

class UpdateObject:
    def __init__(self, main_table):
        self.main_table = main_table
        self.set = []
        self.where_clauses = []
        pass
    

class DeleteObject:
    def __init__(self, main_table):
        self.main_table = main_table
        self.where_clauses = []
