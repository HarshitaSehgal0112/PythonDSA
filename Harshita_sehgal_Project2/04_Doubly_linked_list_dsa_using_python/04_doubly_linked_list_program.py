#In class DLL,define a method
#to insert_at_start to insert the element at the starting of the list
class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class DLL:
    def __init__(self,start=None):
        self.start=start
    def insert_at_start(self,data):
        n=Node(None,data,self.start)
        if self.start is None:
            self.start=n
        else:
            self.start.prev=n
            self.start=n
    def show(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
t1=DLL()
t1.insert_at_start(10)
t1.insert_at_start(20)
t1.insert_at_start(30)
print("Doubly Linked list:")
t1.show()