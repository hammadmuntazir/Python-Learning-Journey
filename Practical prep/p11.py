num1=int(input("Enter value of number 1 :"))
num2=int(input("Enter value of number 2 :"))
num3=int(input("Enter value of number 3 :"))
num4=int(input("Enter value of number 4 :"))

if num1<num2 and num1<num3 and num1<num4:
    print(f"{num1} is minimum")
elif num2<num1 and num2<num3 and num2<num4:
    print(f"{num2} is minimum")
elif num3<num1 and num3<num2 and num3<num4:
    print(f"{num3} is minimum")
else:
    print(f"{num4} is minimum")