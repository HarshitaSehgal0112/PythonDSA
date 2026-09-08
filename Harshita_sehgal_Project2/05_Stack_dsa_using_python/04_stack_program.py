
# stack using list
"""
In stack class,define pop() method to remove top data from the stack
"""
class stack:
    def __init__(self,l1):
        self.l1=l1
    def pop(self):
        if self.l1 is not None:
            return self.l1.pop()
        else:
            raise IndexError("stack is empty")
s1=stack(l1=[10,20,"abc",30])
print("Removed element:",s1.pop())
