
# stack using list
"""
define a method is_empty to check if the stack is empty in stack class
"""
class stack:
    def __init__(self,l1):
        self.l1=l1
    def is_empty(self):
        return len(self.l1)==0
s1=stack(l1=[10,20,'abc',30])
print("Is list empty:",s1.is_empty())



