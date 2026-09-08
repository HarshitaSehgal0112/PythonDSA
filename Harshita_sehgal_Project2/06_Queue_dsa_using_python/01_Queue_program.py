# Queue using list
"""
1 define a class Queue to implement Queue data structure using list. define __init__()
  method to create an empty list object as instance object member of Queue.
2 define a method is_empty to check if the queue is empty in Queue class.
3 In Queue class, define a method enqueue() to add data at the rear end of the queue.
4 In queue class,define a method dequeue() to remove front element from the queue.
5 In queue class,define a method get_front to return front element of the queue.
6 In queue class,define a method get_rear to return rear element of the queue.
7 In queue class,define size() method to return size of the queue that is total
  number of items present in the queue.
"""
class Queue:
    def __init__(self):
        self.l1=[]
    def is_empty(self):
        return len(self.l1)==0
    def enqueue(self,data):
        self.l1.append(data)
    def dequeue(self):
        if not self.is_empty():
            return self.l1.pop(0)
        else:
            raise IndexError("Queue underflow")
    def get_front(self):
        if not self.is_empty():
            return self.l1[0]
        else:
            raise IndexError("Queue underflow")
    def get_rear(self):
        if self.l1 is not None:
            return self.l1[-1]
        else:
            raise IndexError("Queue underflow")
    def size(self):
        return len(self.l1)
q1=Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
print("Elements in queue:",q1.l1)
print("Is queue empty:",q1.is_empty())
print("Removing element:",q1.dequeue())
print("Now queue is:",q1.l1)
print("first element in queue(front):",q1.get_front())
print("last element in queue(rear):",q1.get_rear())
print("size of queue:",q1.size())









