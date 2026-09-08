# define a class DLL to implement doubly linked list with __init__() method
# to create and initialise start reference variable

class Node:
    def __init__(self,item=None,next=None,prev=None):
        self.item=item
        self.next=next
        self.prev=prev
class DLL:
    def __init__(self,start=None):
        self.start=start
t1=DLL(8)
print("start node=",t1.start)