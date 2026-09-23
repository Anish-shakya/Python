import pandas as pd

class DataExt:

    def __init__(self,file_path:str): ##type hing
        self.file_path = file_path

    def fetch_text(self,separator:str):
        ### write your custom logic here
        df = pd.read_csv(self.file_path,sep=separator)
        print(df.head(5))

    def fetch_json(self):
        ### write your custom logic here
        df= pd.read_json(self.file_path)
        print(df.head(5))
       
    def fetch_parquet(self):
        ### write your custom logic here
        df= pd.read_parquet(self.file_path)
        print(df.head(5))
         
obj = DataExt("Files/orders.csv")
obj.fetch_text(",")


