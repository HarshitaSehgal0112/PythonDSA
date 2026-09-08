# stack using singly linked list
"""
1 define a class stack to implement stack data structure using singly linked list
  concept. define init() method to initialise start reference variable and item_count
  variable to keep track of number of elements in the stack.
2 define a method is_empty to check if the stack is empty in stack class.
3. define a method push() to add data onto the stack.
4. define a method pop() to remove top element from the stack.
5. define a method peek() to return top element on the stack.
6. define a method size() to return size of the stack.
"""
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class stack:

    def __init__(self):
        self.start=None
        self.item_count=0
    def is_empty(self):
        return self.start==None
    def push(self,data):
        n=Node(data,self.start)
        self.start=n
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
            data=self.start.item
            self.start=self.start.next
            self.item_count-=1
            return data
        else:
            raise IndexError("stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("stack is empty")
    def size(self):
        return self.item_count
s1=stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("Total number of elements:",s1.item_count)
print("Top element:",s1.peek())
print("Removed top element:",s1.pop())
print("size of data:",s1.size())


