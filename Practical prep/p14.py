#Python program to find largest,smalles and second largest of three number using simple if statmenet
a=int(input("Enter value of a :"))
b=int(input("Enter value of b :"))
c=int(input("Enter value of c :"))

#finding largest number
largest=a
if b>largest:
       largest=b
if c>largest:
    largest=c

#finding smallest number
smallest=a
if smallest>b:
    smallest=b
if smallest>c:
   smallest=c

#finding second largest
second_largest =(a+b+c)-(largest+smallest)

print(f"Largest value = {largest}")
print(f"second largestvalue = {second_largest}")
print(f"smallest value = {smallest}")
