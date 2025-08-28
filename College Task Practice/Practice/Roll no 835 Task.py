n=3
for i in range(1,n+1):
     if(i==1 or i==n):
      print("*"*n,end="")
     else:
        print("*",end="")
        print("  "*(n-2),end="")
        print("*",end="")


#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly
# Get user input
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

# Calculate pay
if hours <= 40:
    pay = hours * rate
else:
    normal_pay = 40 * rate
    overtime_pay = (hours - 40) * (rate * 1.5)
    pay = normal_pay + overtime_pay

# Show result
print("Gross pay:", pay)