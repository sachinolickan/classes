import math
class AreaPerimeter:
    x=math.pi
    def __init__(self,r):
        self.radius=r
    def perimeter(self):
        self.perimeter=2*self.x*self.radius
    def area(self):
        self.area=self.x*self.radius*self.radius
    def display(self):
        print("radius r={}, area={},perimeter={}".format(self.radius,self.area,self.perimeter))
ob=AreaPerimeter(6)
ob.perimeter()
ob.area()
ob.display()
    
    
