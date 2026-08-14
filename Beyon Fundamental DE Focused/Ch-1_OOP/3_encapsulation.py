
class MyClass:
    # Class variables
    var1 = "Anish"
    var2 = "Shakya"

    #Constructor
    def __init__(self,dynamic1,dynamic2,dynamic3):
        self.dynamic1 = dynamic1 ## Public Variable
        self.__dynamic2 = dynamic2 ## Private Variable
        self.dynamic3 = dynamic3

    #methods
    def func1(self):
        print(f"Hello World {self.dynamic1} ")

    def func2(self):
        print(f"Hello Globe {self.__dynamic2}")
    
    def func3(self):
        print(f"Hello Globe {self.dynamic3}")


# Create Python Object
obj = MyClass("ABC","DEF","GHI")



print(obj.dynamic1)

obj.dynamic1="PQR"
print(obj.dynamic1)
### below varible is not a varible __dynamic2 it's new variable so the code will not throw the error
obj.dynamic2="STU"
print(obj.dynamic2)

