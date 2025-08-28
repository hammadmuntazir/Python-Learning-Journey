a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))

if a>b:
    if a>c:
        print("a is greatest of three number and it's value = ",a)
    else:
        print("c is greatest of three number and it's value =",c)
else:
    if b>c:
        print("b is the greatest of three number and it's value =",b)
    else:
        print("c is greatest of three number and it's value = ",c)