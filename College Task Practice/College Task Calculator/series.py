print("Fabonic series")
n=int(input("Enter number : "))
a,b= 0,1
print(a,b,end=" ")
i=2
while i<n:
    next=a+b
    print(next,end=" ")
    a=b
    b=next
    i=i+1