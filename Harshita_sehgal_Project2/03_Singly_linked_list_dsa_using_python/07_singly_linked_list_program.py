# In class SLL,define a method insert_after() to insert a new node after a given node

class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start=None):
        self.start=start

    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
    def show(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
t1=SLL(Node(10))
t1.start.next=Node(20)
t1.start.next.next=Node(30)
print("Before insertion:")
t1.show()

t1.insert_after(t1.start.next,25)
print("\nAfter insertion:")
t1.show()

