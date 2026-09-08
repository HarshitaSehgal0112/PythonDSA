
"""
define a class SLL and
define a method insert_at_start() to insert an element at the starting of the list
"""
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start=None):
        self.start=start
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
    def show(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
t1=SLL()
print("Linked list:")
t1.insert_at_start(10)
t1.insert_at_start(20)
t1.insert_at_start(15)
t1.show()



