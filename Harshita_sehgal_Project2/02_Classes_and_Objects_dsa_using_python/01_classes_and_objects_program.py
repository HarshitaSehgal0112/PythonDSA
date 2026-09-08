
# define a python class Person with instance object variables name and age.
# set instance object variables in __init__() method.
# also define show() method to display name and age of a person.

class Person:
    def __init__(self):
        self.name="Harshita"
        self.age=20
    def show(self):
         print("Name=",self.name)
         print("Age=",self.age)
t1=Person()
t1.show()


