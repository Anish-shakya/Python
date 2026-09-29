class company:

    title:str ="Media Agency"

    def __init__(self,company_name:str):
        self.company_name:str = company_name

    def info(self):
        print(f'Company Name : {self.company_name}')
        return f"Company Name: {self.company_name}"
 
class manager(company):
     
    def __init__(self,manager_name:str,company_name:str):  ## we need to pass the argument required for parent class as well (i.e Company Name)
        self.manager_name:str =manager_name
        self.company_name:str = company_name
     
    def info(self):
        response = company.info(self) ##or super.info() to call the function from parent class but only works for single level inheritance 
        print(f"The manager: {self.manager_name} {response} ")
        return f"The manager: {self.manager_name}"
    
class employee(manager):
    
    def __init__(self,employee_name:str,manager_name:str,company_name:str):
        self.employee_name:str = employee_name
        self.manager_name:str = manager_name
        self.company_name:str = company_name
        
    def info(self):
        response = manager.info(self)
        print(f"The employee:{self.employee_name}, {response}")
        

obj = employee("Anish Shakya","Sanan Maharjan","Omnicom Media Group")

obj.info()
        