

# define a class Book with instance object variables bookid, title and price.
# initialise them via __init__() method.
# also define method to show book variables.

class Book:
    def __init__(self,bookid,title,price):
        self.bookid=bookid
        self.title=title
        self.price=price
    def show(self):
        print("Bookid=",self.bookid)
        print("Title",self.title)
        print("Price=",self.price)
t1=Book(12345,"Learning Python",650)
t1.show()

