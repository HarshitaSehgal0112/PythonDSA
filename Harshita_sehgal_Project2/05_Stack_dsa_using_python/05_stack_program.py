
# stack using list
"""
In stack class,define peek() method to return top data on the stack
"""
class stack:
    def __init__(self):
        self.l1=[10,20,30,40]
    def peek(self):
        if self.l1 is not None:
            return self.l1[-1]
        else:
            raise IndexError("stack is empty")
s1=stack()
print(s1.peek())