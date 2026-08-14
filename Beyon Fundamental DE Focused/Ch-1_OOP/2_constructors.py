
class MyClass:
    # Class variables
    var1 = "Anish"
    var2 = "Shakya"

    #Constructor
    def __init__(self,dynamic1,dynamic2,dynamic3):
        self.dynamic1 = dynamic1
        self.dynamic2 = dynamic2
        self.dynamic3 = dynamic3

    #methods
    def func1(self):
        print(f"Hello World {self.dynamic1} ")

    def func2(self):
        print(f"Hello Globe {self.dynamic2}")
    
    def func3(self):
        print(f"Hello Globe {self.dynamic3}")


# Create Python Object
obj = MyClass("ABC","DEF","GHI")
## Standard apporach
obj.func1()
obj.func2()
obj.func3()

#Another way to call this function 
MyClass.func1(obj)


obj_new = MyClass("JKL","MNO","PQR")
obj_new.var2="Changed"
print(obj_new.var2)
obj_new.func2()

