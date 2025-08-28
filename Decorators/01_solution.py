# import time

# def timer(func):
#     def  wrapper(*args, **kwargs):
#         result=func(*args, **kwargs)
#         return result

# A decorator is a function that takes 
# another function as input and returns a
#  modified version of that function. 
# Think of it like a wrapper that adds extra functionality.

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()
# my_decorator(Say_hello)()  #assy bi krskty ho

def greet(fx):
    def mfx():
        print('Good Morning')
        fx()
        print('Thanks for using Function')
    return mfx
@greet
def hello():
    print('Hello world')
hello()