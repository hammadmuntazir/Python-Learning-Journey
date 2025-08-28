'''
               Problem 3:
Create a class with a class attribute a; create an object from it and set ‘a’
directly using ‘object.a = 0’. Does this change the class attribute?
'''
class demo:
    a=1
b=demo()
print(b.demo)#Prints class attribute because instance attribute is not present
b.demo=5# instance attribute sets
print(b.demo)#print instance attributes because instance attribute is present
print(demo.a)#No ,it does not change class attribute
