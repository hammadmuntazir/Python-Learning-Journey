#write a program which tells whether age entered is of child,teenager,adult
age=int(input("Enter your age: "))
if age<13:
    print("Child")
elif age<20:
    print("Teenager")
elif age<60:
    print("Adult")
else:
    print("Senior")