class company:

    title:str ="Media Agency"

    def __init__(self,company_name:str):
        self.company_name:str = company_name

    def info(self):
        print(f'Company Name : {self.company_name}')
        return f"Company Name: {self.company_name}"
 
class client_company:

    title:str ="Chanel"

    def __init__(self,client_company_name:str):
        self.client_company_name:str = client_company_name

    def info(self):
        print(f'Company Name : {self.client_company_name}')
        return f"Company Name: {self.client_company_name}"
    
class employee(company,client_company):
    
    def __init__(self,employee_name:str,company_name:str,client_company_name:str):
        self.employee_name:str = employee_name
        self.company_name:str = company_name
        self.client_company_name:str = client_company_name
        
    def info(self):
        response1 =company.info(self)
        response2=client_company.info(self)
        print(f"The employee: {self.employee_name},{response1},{response2}")
        return f"The employee: {self.employee_name},{response1},{response2}"

obj = employee("Anish Shakya","Omnicom Media Group","Chanel")
obj.info()
        
        