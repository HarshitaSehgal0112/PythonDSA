

# define a class circle with instance object variable radius.
# provide setter and getter for radius.
# also define getArea() and getCircumference methods.
class circle:
    def __init__(self,radius):
        self.radius=radius
    def setradius(self,radius):
        self.radius=radius
    def getradius(self):
        return self.radius
    def getArea(self):
        return 3.14*self.radius*self.radius
    def getCircumference(self):
        return 2*3.14*self.radius
t1=circle(5)
print("radius=",t1.getradius())
print("Area=",t1.getArea())
print("Circumference=",t1.getCircumference())
