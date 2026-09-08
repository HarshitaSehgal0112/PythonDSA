# Queue using extending list

"""
1 define a class Queue to implement Queue data structure using list.
2 define a method is_empty to check if the queue is empty in Queue class.
3 In Queue class, define a method enqueue() to add data at the rear end of the queue.
4 In queue class,define a method dequeue() to remove front element from the queue.
5 In queue class,define a method get_front to return front element of the queue.
6 In queue class,define a method get_rear to return rear element of the queue.
7 In queue class,define size() method to return size of the queue that is total
  number of items present in the queue.
"""
class Queue(list):
    def is_empty(self):
        return len(self)==0
    def enqueue(self,data):
        self.append(data)
    def dequeue(self):
        if not self.is_empty():
            return self.pop(0)
        else:
            raise IndexError("Queue underflow")
    def get_front(self):
        if not self.is_empty():
            return self[0]
        else:
            raise IndexError("Queue underflow")
    def get_rear(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Queue underflow")
    def size(self):
        return len(self)
q1=Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
print("Elements in queue:",q1)
print("Is queue empty:",q1.is_empty())
print("Dequeue:",q1.dequeue())
print("front:",q1.get_front())
print("Rear:",q1.get_rear())
print("Now queue has:",q1.size())



