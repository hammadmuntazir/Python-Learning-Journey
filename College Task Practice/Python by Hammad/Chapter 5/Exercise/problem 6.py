"""6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
value and use key as their names. Assume that the names are unique.
"""
'''d={}
name = input("Enter  friends name :")
lang=  input("Enter Language name: ")

d.update({name:lang})

name = input("Enter  friends name :")
lang=  input("Enter Language name: ")

d.update({name:lang})

name = input("Enter  friends name :")
lang=  input("Enter Language name: ")

d.update({name:lang})

name = input("Enter  friends name :")
lang=  input("Enter Language name: ")

d.update({name:lang})
print(d)

#7. If the names of 2 friends are same; what will happen to the program in problem 6 ?
#key ki value update ho jaye gi bs

#8. If languages of two friends are same; what will happen to the program in problem 6?
'''
d={}
for i in range(0,4):
    name=input("Enter friend name :")
    lang=input("Enter language of friend:")
    d.update({name:lang})
print(d)