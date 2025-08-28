'''
Determine if a year is a leap year.(Leap years are divided by 4, but not by 100 unless
also divisble by 400).
'''
year = int(input("Enter the year "))
if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
  print(year ,"is leap year")
else:
    print(year,"is not leap year")