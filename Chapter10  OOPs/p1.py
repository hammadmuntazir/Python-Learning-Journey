import math

class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def  cicumference(self):
        return 2 * math.pi *self.radius

radius =float(input('Enter Radiuse of Circle:'))
circle=Circle(radius)
print('Area of Circle:', circle.area())
print('Circumference of Circle:', circle.cicumference())