#maan lo mujhy aik function banana hai jo n ka factorial deta hai
#factorial (n)=n*factorial (n-1)
#jo code bohat si lines mn likhty vo 4 line mn likh diagh
def factorial(n):
    if (n==1 or n==0):
        return 1
    return n*factorial(n-1)
n=int(input("Enter a number: "))
print("The factorial of",n,"is",factorial(n))