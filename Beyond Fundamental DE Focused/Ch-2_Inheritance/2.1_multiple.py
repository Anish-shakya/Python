class company:

    title:str ="Media Agency"

    def __init__(self,company_name:str):
        self.company_name:str = company_name

    def info(self):
        print(f'Company Name : {self.company_name}')
        return f"Company Name: {self.company_name}"
 
class employee(company): ### Inherite the company class

    def __init__(self,employee_name:str,company_name:str):  ## we need to pass the argument required for parent class as well (i.e Company Name)
        self.employee_name:str =employee_name
        self.company_name:str = company_name

    def info(self):
        response = company.info(self) ##or super.info() to call the function from parent class but only works for single level inheritance 
        print(f"The employee: {self.employee_name} {response} ")

class contractor(employee):
    
    def __init__(self,contractor_name:str,company_name:str):  ## we need to pass the argument required for parent class as well (i.e Company Name)
        self.contractor_name:str =contractor_name
        self.company_name:str = company_name

    def info(self):
        response = company.info(self) ##or super.info() to call the function from parent class but only works for single level inheritance 
        print(f"The employee: {self.contractor_name} {response} ")

emp1 =employee('Anish Shakya','Omnicom Media Group')
emp1.info()

print('--------------------------------------------')

emp2 =contractor('Manish Shakya','Omnicom Media Group')
emp2.info()