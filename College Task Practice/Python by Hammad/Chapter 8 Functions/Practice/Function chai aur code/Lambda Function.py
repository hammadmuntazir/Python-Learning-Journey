'''
Create a lambda function to compute the cube of a number.
'''
'''def add(a,b):
    return a+b
result=add(5,6)'''
#lambda function hota hai jiska name nai hota
#lambda ky baad hum directly function likh skty hain
cube = lambda x: x ** 3
#is puray portion ka koi name nai hai mgr is portion ka result mein ny store
#krlia hai cube ky andar
print(cube(3))
#lambda mostly use in frameworks
#is defination ko ksi aur variable mn nai daal skty
print(cube(45))