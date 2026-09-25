class MyClass:
    # Class Variables 
    var1="Anish"
    var2="Shakya"

    ## Instance variable
    def __init__(self,dyn1,dyn2,dyn3):
        self.dyn1=dyn1 # public Variable
        self.__dyn2=dyn2 # Private Variable with __ double underscore
        self._dyn3=dyn3 # Protected Variable It is not a private but it indicated developer that it is protected variable
    
    def func1(self):
        print(f'Hello World,{self.dyn1}')
    
    def func2(self):
        print(f'Hello Globe,{self.__dyn2}')
    
    def fun3(self):
        print(f'Hello Globe,{self._dyn3}')

obj = MyClass("abc","def","xyz")

print(obj.dyn1)
obj.dyn1 = "ABC"
obj.func1()


# This will not give the error as this will create new variable called dyn2 which is not related to __dyn2 
obj.dyn2="stu"
print(obj.dyn2) 

obj.func2() ## here dyn2 is not accessable at all due to private access modfier so it gives Hello Globe, def

print(obj._dyn3)
obj.fun3()
