# recursion programs
"""
1 write a recursive function to calculate sum of first N natural numbers.
2 write a recursive function to calculate sum of first N even natural numbers.
3 write a recursive function to calculate sum of first N odd natural numbers.
4 write a recursive function to calculate sum of squares of first N natural numbers.
5 write a recursive function to calculate factorial of a number.
"""
def f1(n):                                           #1
    if n==1:
        return 1
    return n+f1(n-1)

def f2(n):                                          #2
    if n==1:
        return 2
    return 2*n+f2(n-1)

def f3(n):                                           #3
    if n==1:
        return 1
    return 2*n-1+f3(n-1)

def f4(n):                                            #4
    if n==1:
        return 1
    return n*n+f4(n-1)

def f5(n):                                            #5
    if n==0:
        return 1
    return n*f5(n-1)
print(f1(10))
print(f2(10))
print(f3(10))
print(f4(10))
print(f5(10))