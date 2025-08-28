a=int(input("value of 1st number :"))
b=int(input("value of 2nd number :"))
c=int(input("value of 3rd number :"))
d=int(input("value of 4th number :"))

if a>b and a>c and a>d:
    print(f"{a} is maximum")
elif b>a and b>c and b>d:
    print(f"{b} is maximum")
elif c>a and c>b and c>d:
    print(f"{c} is maximum")
else:
    print(f"{d} is maximum")