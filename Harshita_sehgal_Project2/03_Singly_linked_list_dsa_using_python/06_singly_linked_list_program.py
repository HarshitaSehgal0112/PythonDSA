# In class SLL,define a method search() to find the node with specified element value

class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
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
t1=SLL(Node(10))
t1.start.next=Node(20)
t1.start.next.next=Node(30)
print("Linked list:")
t1.show()

result=t1.search(int(input("\nEnter data:")))
if result is not None:
      print("\nElement found")
else:
      print("\n Element not found")


