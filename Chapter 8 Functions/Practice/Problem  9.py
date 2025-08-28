#8. Write a python function to print multiplication table of  given number.
n=int(input("enter num :"))
def multiply(n):
   for i in range(1,11):
        print(n,"*", i ,"=", n*i)
multiply(n)