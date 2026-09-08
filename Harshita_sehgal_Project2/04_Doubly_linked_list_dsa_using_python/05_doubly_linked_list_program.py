#In class DLL,define a method insert_at_last to insert the element to the ending of list
class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class DLL:
    def __init__(self,start=None):
        self.start=start
    def insert_at_last(self,data):
        temp=self.start
        if not self.start is None:
             while temp.next is not None:
                temp=temp.next
        n=Node(temp,data,None)
        if temp==None:
            self.start=n
        else:
            temp.next=n
    def show(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
t1=DLL()
t1.insert_at_last(10)
t1.insert_at_last(20)
t1.insert_at_last(30)
print("Doubly linked list:")
t1.show()