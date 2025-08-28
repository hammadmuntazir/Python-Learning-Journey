'''
Problem 4:
4. Add a static method in problem 2, to greet the user with hello.

'''

class Calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"The square is {self.n**2}")

    def square_root(self):
        print(f"The square root is  {self.n**(1/2)}")

    def cube(self):
         print(f"The cube is {self.n**3}")

    def cube_root(self):
        print(f"The cube root is {self.n**(1/3)}")

    @staticmethod
    def greet():
        print("Good Morning")
a=Calculator(4)
a.greet()
a.square()
a.cube()
a.square_root()
a.cube_root()
