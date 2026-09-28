class MyClass:

    my_var = 100

    #Constructor or Dunder method or magic method
    def __init__(self):
        print("This is the constructor method")

     #Constructor or Dunder method or magic method
    def __str__(self):
        return "This is the string representation of the object"

    @classmethod ## Decorator for class variable
    def _ChangeValue(cls,new_value): ## Protected to let dev team know not to change anything in this unless you know what you are doing
        cls.my_var=new_value
    
    @staticmethod
    def dummy(): ## we don't need to pass the self or cls as this is the aditional function that doesn't need access to object or class
        print("This is a dummy method")


# obj = MyClass()
# print(obj.my_var)
# obj._ChangeValue(200)
# print(obj.my_var)

# obj1=MyClass()
# print(obj1.my_var)

# obj2=MyClass()
# obj2.dummy()

obj3=MyClass()
print(obj3)
