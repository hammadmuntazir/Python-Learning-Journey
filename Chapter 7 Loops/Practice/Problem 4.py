#4. Write a program to find whether a given number is prime or not.
n = int(input("Enter a number: "))

for i in range(2,n):#n here mean n-1
    if (n % i == 0):
        print(n,"is not a prime number")
        break
else :
    print(n,"is a prime number")