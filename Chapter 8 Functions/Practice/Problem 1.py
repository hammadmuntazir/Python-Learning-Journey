#1. Write a program using functions to find greatest of three numbers.
def greatest(a,b,c):
    if (a>b and a>c):
        print(a,"is greater than ",b,"and",c)
    elif (b>a and b>c):
        print(b,"is greater than ",a,"and",c)
    else:
        print(c,"is greater than ",a,"and",b)
a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
c= int(input("Enter third number: "))
greatest(a,b,c)