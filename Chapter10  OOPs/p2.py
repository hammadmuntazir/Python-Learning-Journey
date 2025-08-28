class Calculator:
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        if b==0:
            print("Error: Division by zero is not allowed.")
        else:
            return a/b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
calculate=Calculator()
result=calculate.add(a,b)
print("Addition result:", result)

result=calculate.subtract(a,b)
print("Subtraction result:", result)

result=calculate.multiply(a,b)
print("Multiplication result:", result)

result=calculate.divide(a,b)
if result is not None:
    print("Division result:", result)
else:
    print("Division operation was not performed due to an error.")