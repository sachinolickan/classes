class Area:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        self.area=self.length*self.breadth
    def display(self):
        print("area of the rectangle for the values l={} and b={} is a={}".format(self.length,self.breadth,self.area))
ob=Area(3,2)
ob.area()
ob.display()

ob1=Area(4,2)
ob1.area()
ob1.display()

ob3=Area(5,3)
ob3.area()
ob3.display()
