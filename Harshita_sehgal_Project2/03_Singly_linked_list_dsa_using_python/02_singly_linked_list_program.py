




""" define a class SLL to implement singly linked list with __init__() method
 to create and initialise start reference variable
"""
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start=None):
        self.start=start
t1=SLL(7)
print("start=",t1.start)

