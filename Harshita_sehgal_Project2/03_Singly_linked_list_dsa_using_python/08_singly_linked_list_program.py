# In class SLL,define a method to delete_first and delete_last node of the linked list
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self. next=next
class SLL:
    def __init__(self,start=None):
        self.start=start

    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next

    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None

    def show(self):
             temp=self.start
             while temp is not None:
                print(temp.item,end=' ')
                temp=temp.next
t1=SLL(Node(10))
t1.start.next=Node(20)
t1.start.next.next=Node(30)
t1.start.next.next.next=Node(40)
print("Before deleting:")
t1.show()

t1.delete_first()
print("\nAfter deleting first node:")
t1.show()
t1.delete_last()
print("\n After deleting last node:")
t1.show()
