
class WarehouseLoader:
    def __init__(self,warehouse_name,warehouse_id):
        self.warehouse_name = warehouse_name
        self.warehouse_id = warehouse_id
    
    def load(self,data):
        print(f"Loading data into {self.warehouse_name} warehouse with ID {self.warehouse_id}")
        for record in data:
            print(f"Loaded record: {record}")