""" define a class Node to describe a node of a singly linked list
"""
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
t1=Node(10,8)
print("item=",t1.item)
print("next=",t1.next)
