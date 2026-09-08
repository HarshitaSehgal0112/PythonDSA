# stack using
# extending list
"""
1. define a class stack to implement stack data structure by extending list class.
2. define a method is_empty to check if the stack is empty or not in stack class.
3. define a method push() to add data onto the stack.
4. define a method pop() to remove top element from the stack.
5. define a method peek() to return top element on the stack.
6. define a method size() to return size of the stack.
7. implement a way to restrict use of insert() method of class list from stack object
"""
class stack(list):
    def is_empty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("stack is empty")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("stack is empty")
    def size(self):
        return len(self)
    def insert(self,index,data):
        raise AttributeError("No attribute 'insert' in stack")
s1=stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("Is list empty:",s1.is_empty())
print("stack list is=",s1)
print("Removed top element is:",s1.pop())
print("Top element is:",s1.peek())
print("Size of stack list is:",s1.size())


