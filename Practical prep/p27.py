married=input("enter yes or no")
gender=input("Enter male or female")
age=int(input("Enter your age"))

if married=="yes":
    print("Eligible for insurance")

elif married!="yes" and gender=="male" and age>30:
    print("Eligible for insurance")

elif married !="yes" and gender=="female" and age>25:
    print("Eligible for insurance")
else:
    print("Not  is not eligible for insurance")