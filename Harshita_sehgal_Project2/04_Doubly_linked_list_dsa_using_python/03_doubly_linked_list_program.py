# define a class is_empty to check that the linked list is empty in DLL

class Node:
    def __init__(self,item=None,next=None,prev=None):
        self.item=item
        self.next=next
        self.prev=prev
class DLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
       return self.start is None
t1=DLL(8)
print("Is linked list empty=",t1.is_empty())