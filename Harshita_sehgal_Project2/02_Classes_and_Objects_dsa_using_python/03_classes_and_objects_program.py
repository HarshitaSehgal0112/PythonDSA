
# define a class rectangle with length and breadth as instance objects variables.
# provide setDimensions() and showDimensions() and getArea() methods in it.

class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def setDimensions(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def getArea(self):
        return self.length*self.breadth
    def showDimensions(self):
        print("length=",self.length)
        print("breadth=",self.breadth)
t1=rectangle(5,6)
t1.showDimensions()
print("Area=",t1.getArea())

