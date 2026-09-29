#### creating own decorator function

def my_decorator(func):
    def mainfunc(*args):
        print("Before calling the function")
        response = func(*args)
        print("After calling the function")
        return response
    return mainfunc



@my_decorator
def fetch_date(url:str,path:str):
    return f"fecthing data from {url} with path {path}"

response = fetch_date("https://www.google.com","/search")
print(response)