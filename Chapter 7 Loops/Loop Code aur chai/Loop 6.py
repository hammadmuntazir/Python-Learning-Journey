#Computer Factorial of a number using loop
'''
n=int(input("Inputr number"))
count=1
for i in range(1,n+1):
    count*=i
print("Factorial of ",n,"=",count)'''
number=int(input("Enter number:"))
factorial=1
while number>0:
    factorial =factorial*number
    number=number-1
print(factorial)