
# In a class SLL,define a method insert_at_last()
# to insert the element at the end of the list

class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start=None):
        self.start=start
    def insert_at_last(self,data):
        n=Node(data)
        if not self.start is None:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n
    def show(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
t1=SLL()
print("Linked list:")
t1.insert_at_last(10)
t1.insert_at_last(20)
t1.insert_at_last(30)
t1.show()