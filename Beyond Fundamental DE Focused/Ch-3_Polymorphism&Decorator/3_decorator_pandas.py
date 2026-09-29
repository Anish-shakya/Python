

def pandasdecorator(func):
    def maifunc(*args):
        response = func(*args)
        response.to_parquet("Beyond Fundamental DE Focused\\Ch-3_Polymorphism&Decorator\\orders.parquet")
        return response.head()
    return maifunc


@pandasdecorator
def csv_to_parquet(file_path:str):
    import pandas as pd
    df = pd.read_csv(file_path)
    return df
        
csv_to_parquet("Beyond Fundamental DE Focused\\Ch-3_Polymorphism&Decorator\\orders.csv")