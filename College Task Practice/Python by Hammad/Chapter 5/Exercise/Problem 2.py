""" Write a program to input eight numbers from the user and display all the unique
numbers (once)."""
'''s=set()
s1 = input("Enter number 1 :")
s.add(s1)
s2 = input("Enter number 2 :")
s.add(s2)
s3 = input("Enter number 3 :")
s.add(s3)
s4 = input("Enter number 4 :")
s.add(s4)
s5 = input("Enter number 5 :")
s.add(s5)
s6 = input("Enter number 6 :")
s.add(s6)
s7 = input("Enter number 7 :")
s.add(s7)
s8 = int(input("Enter number 8 :"))
s.add(s8)
print("All numbers are displayed as \n",s)
#3. Can we have a set with 18 (int) and '18' (str) as a value in it?
#3 yes , just make s8=int(input("Enter number 8:"))'''
s=set()
for i in range(9):
   n=int(input("Enter number"))
   s.add(n)
print(s)