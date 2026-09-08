# priority queue using list
"""
1 define a class priorityQueue to implement priorityQueue data structure using list.
  and define __init__() method to create a list object (initially empty).
2 define push() method in priorityQueue class to insert new data with given priority.
3 define pop() method in priorityQueue class, which returns the highest priority data
  stored in priority Queue data structure. Raise exception if priority queue is empty.
4 define is_empty method in priorityQueue class to check if the priority queue is empty.
5 In class priorityQueue, define a method size to return the number of elements present
   in the priority queue.
"""
class priorityQueue

    def __init__(self):
        self.l1=[]
    def is_empty(self):
        return len(self.l1)==0
    def push(self,data,priority):
        index=0
        while index<len(self.l1) and self.l1[index][1]:
            index+=1
        self.l1.insert(index,(data,priority))
    def pop(self):
        if not self.is_empty():
            return self.l1.pop(0)[0]
        else:
            raise IndexError("priority queue is empty")
    def size(self):
        return len(self.l1)
p1=priorityQueue()
p1.push("Harshita",1)
p1.push("Muskan",7)
p1.push("Lishika",2)
p1.push("Ronit",5)
p1.push("Ashima",8)
p1.push("Varun",4)
print("priority queue is=",p1.l1)
while not p1.is_empty():
    print(p1.pop())















