a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))

if a<b:
    if a<c:
        print("a is smallest of three number and it's value = ",a)
    else:
        print("c is smallest of three number and it's value =",c)
else:
    if b<c:
        print("b is the smallest of three number and it's value =",b)
    else:
        print("c is smallest of three number and it's value = ",c)