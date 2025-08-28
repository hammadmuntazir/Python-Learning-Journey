'''#1. Write a program to print multiplication table of a given number using for loop.
i= int(input("Enter a number: "))
count=1
i=i*count
while count<=10:
    print(i,"*",count,"=",i*count )
    count=count+1
'''
n=int(input("Enter a number: "))

for i in range(1,11):
    print(f"{n} * {i} = {n*i}")