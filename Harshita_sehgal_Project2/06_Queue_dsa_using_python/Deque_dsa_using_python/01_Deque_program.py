# Deque using list
"""
1 define a class deque to implement deque data structure using list. define __init__()
  method to create an empty list object as instance object member of deque.
2 define a method is_empty to check if the deque is empty in deque class.
3 In Queue class, define a method insert_front() to add data at the front end of the deque.
4 In queue class,define a method insert_rear() to add data at rear element from the queue.
5 In queue class,define a method delete_front() to remove front element from the queue.
6 In queue class,define a method delete_rear() to remove rear element from the queue.
7 In queue class,define a method get_front to return front element of the queue.
8 In queue class,define a method get_rear to return rear element of the queue.
9 In queue class,define size() method to return size of the queue that is total
  number of items present in the queue.
"""
class Deque:
    def __init__(self):
        self.l1=[]
    def is_empty(self):
        return len(self.l1)==0
    def insert_front(self,data):
        self.l1.insert(0,data)
    def insert_rear(self,data):
        self.l1.append(data)
    def delete_front(self):
        if not self.is_empty():
            return self.l1.pop()
        else:
            raise IndexError("Deque is empty")
    def delete_rear(self):
        if not self.is_empty():
            return self.l1.pop()
        else:
            raise IndexError("Deque is empty")
    def get_front(self):
        if not self.is_empty():
            return self.l1[0]
        else:
            raise IndexError("Deque is empty")
    def get_rear(self):
        if not self.is_empty():
            return self.l1[-1]
        else:
            raise IndexError("Deque is empty")
    def size(self):
        return len(self.l1)
d1=Deque()
d1.insert_front(10)
d1.insert_front(20)
d1.insert_rear(30)
d1.insert_rear(40)
print("Deque is:",d1.l1)
print("get_front element is:",d1.get_front())
print("get_rear element is:",d1.get_rear())
print("Total elements in Deque:",d1.size())
print("Removing last element from deque:",d1.delete_rear())
print("Now deque has",d1.size(),"elements")






