
# stack using list
"""
In stack class,define push() method to add data into the stack
"""
class stack:
    def __init__(self):
        self.l1=[10,30,"Python",9.3,50]
    def push(self,data):
        self.l1.append(data)
        self.l1.insert(1,data)
s1=stack()
s1.push(20)
s1.push("Hie")
print("final list after push operation:",s1.l1)