
# stack using list
"""
In stack class,define size() method to return size of the stack.
"""
class stack:
    def __init__(self):
        self.l1=[10,20,30,40]
    def size(self):
       return len(self.l1)
s1=stack()
print("size of stack:",s1.size())