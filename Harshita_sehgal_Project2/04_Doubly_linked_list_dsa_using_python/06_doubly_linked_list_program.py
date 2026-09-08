# In class DLL,define a method search() to find the node with specified element value

class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class DLL:
    def __init__(self,start=None):
        self.start=start
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    def show(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
t1=DLL(Node(item=10))
t1.start.next=Node(item=20)
t1.start.next.next=Node(item=30)
print("Doubly linked list:")
t1.show()
result=t1.search(int(input("\nEnter the data:")))
if result is not None:
    print("\nElement found")
else:
    print("Element not found")