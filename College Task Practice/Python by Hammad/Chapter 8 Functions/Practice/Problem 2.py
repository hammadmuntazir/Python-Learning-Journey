#2. Write a python program using function to convert Celsius to Fahrenheit.
# formula  c/5 =(f-32)/9
# #c=5*(f-32)/9
# f=int(input("Enter the temperature in Fahrenheit: "))
# c= 5*(f-32)/9
#
# print(c)

def f_to_c(f):
    return 5*(f-32)/9

f=int(input("Enter the temperature in Fahrenheit: "))
c=f_to_c(f)
print(round(c,2),"°c")

