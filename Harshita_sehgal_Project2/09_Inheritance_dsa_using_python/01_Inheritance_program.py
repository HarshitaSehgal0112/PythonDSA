# inheritance program
class Person:
    def __init__(self,f_name,l_name):
        self.f_name=f_name
        self.l_name=l_name
    def display(self):
        print("f_name=",self.f_name)
        print("f_name=", self.l_name)
class student(Person):
    def __init__(self,f_name,l_name):
        Person.__init__(self,f_name,l_name)
t1=student("Harshita","sehgal")
t1.display()
