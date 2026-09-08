# recursion program
"""
1 write a recursivn function to print first n natural numbers.
2 write a recursivn function to print first n natural numbers in reverse order.
3 write a recursive function to print first n odd natural numbers.
4 write a recursive function to print first n even natural numbers.
5 write a recursive function to print first odd natural numbers in reverse order.
6 write a recursive function to print first even natural numbers in reverse order.
"""
def printN(n):                                        #1
    if n>0:
        printN(n-1)
        print(n,end=' ')
print("first 10 natural numbers are:")
printN(10)
print("\n")
def printNreverse(n):                                 #2
    if n>0:
        print(n,end=' ')
        printNreverse(n-1)
print("first 10 natural numbers in reverse order:")
printNreverse(10)
print("\n")
def printNodd(n):                                     #3
    if n>0:
        printNodd(n-1)
        print(2*n-1,end=' ')
print("first 10 odd numbers are:")
printNodd(10)
print("\n")
def printNeven(n):                                    #4
    if n>0:
        printNeven(n-1)
        print(2*n,end=' ')
print("first 10 even numbers are:")
printNeven(10)
print("\n")
def printNreverseodd(n):                              #5
    if n>0:
        print(2*n-1,end=' ')
        printNreverseodd(n-1)
print("first 10 odd numbers in reverse order:")
printNreverseodd(10)
print("\n")
def printNreverseeven(n):                             #6

    if n>0:
        print(2*n,end=' ')
        printNreverseeven(n-1)
print("first 10 even numbers in reverse order:")
printNreverseeven(10)








