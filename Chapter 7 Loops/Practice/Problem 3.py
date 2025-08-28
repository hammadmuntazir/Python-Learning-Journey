#3. Write a program to print multiplication table of a given number using for loop.
# Attempt problem 1 using while loop.
n= int(input("Enter a number: "))
i=1
while (i<11):
    print(f"{n} *{i} = {n*i}")
    i+=1