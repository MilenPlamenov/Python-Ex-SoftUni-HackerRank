# class MyClass:
#     def __str__(self):
#         return str(self.__class__)
#
#
# instance = MyClass()
# print(instance)

# The __name__ attribute gives the name originally given to the class. Any copies will keep the name. For example


# class Person:
#     def __str__(self):
#         return self.__class__.__name__
#
#
# SecondClass = Person
#
# instance = SecondClass()
# print(instance)


# ----------------------------------------------------------------------------------------------------------------------
# Magic methods

# 1 __new__() method
# In Python the __new__() magic method is implicitly called before the __init__() method.
# The __new__() method returns a new object, which is then initialized by __init__().

# ___________________________________________________
# example
# class Employee:
#     def __new__(cls):
#         print("__new__ magic method is called")
#         inst = object.__new__(cls)
#         return inst
#
#     def __init__(self):
#         print("__init__ magic method is called")
#         self.name = 'Satya'
# ___________________________________________________

# >>> emp = Employee()
# __new__ magic method is called
# __init__ magic method is called
# Thus, the __new__() method is called before the __init__() method.


# 2 __str__() method
# __str__() is overridden to return a printable string representation of any user defined class.

# _____________________________________________________________

# example
# class Employee:
#     def __init__(self):
#         self.name = 'Pesho'
#         self.salary = 10000
#
#     def __str__(self):
#         return f"Name - {self.name}, salary - {self.salary}"
# _____________________________________________________________

# 3 __add__() method



