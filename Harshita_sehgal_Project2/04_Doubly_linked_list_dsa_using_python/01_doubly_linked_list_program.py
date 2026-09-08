# define a class Node to describe a node of a doubly linked list

class Node:
    def __init__(self,item=None,next=None,prev=None):
        self.item=item
        self.next=next
        self.prev=prev
t1=Node(4,7,5)
print("item=",t1.item)
print("next=",t1.next)
print("previous=",t1.prev)
