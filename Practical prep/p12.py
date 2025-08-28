import cmath
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))
x1 = None
x2 = None
disc = b**2 - 4*a*c
if disc == 0:
    x1 = x2 = -b / (2*a)
    print("Roots are real and equal")
    print(f"x1 = {x1}, x2 = {x2}")
elif disc > 0:
    sqrt_disc = cmath.sqrt(disc)  # Or use math.sqrt for real roots
    x1 = (-b + sqrt_disc) / (2*a)
    x2 = (-b - sqrt_disc) / (2*a)
    print("Roots are real and different")
    print(f"x1 = {x1}, x2 = {x2}")
else:  # disc < 0 (complex roots)
    sqrt_disc = cmath.sqrt(disc)
    x1 = (-b + sqrt_disc) / (2*a)
    x2 = (-b - sqrt_disc) / (2*a)
    print("Roots are complex conjugates")
    print(f"x1 = {x1}, x2 = {x2}")
'''
x1=-b+cmath.sqrt[(b**2-4ac)/2a]
x2==b-cmath.sqrt[(b**2-4ac)/2a]

if discriminant=0: roots are real and equal
if disc>0:roots are real and different
if disc<0:roots are imaginary

#Python uses j for imaginary numbers.
'''