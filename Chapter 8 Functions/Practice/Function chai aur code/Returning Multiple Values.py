'''
Create a function that returns both the area and circumference
of a circle given its radius
'''
import math
def circle_stats(radius):
    circumference=2*math.pi*radius
    area=math.pi*radius**2
    return area,circumference
#return ky baad function mn execution line calculate nai hoti
#jtni value return horahi usi hissab sy handle krna hoga
a,b=circle_stats(10)
print("Area =",a.__floor__(),"Cirumference",b.__floor__())