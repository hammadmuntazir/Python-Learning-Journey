'''
#Function with **kwargs
Problem:Create a function that accepts any number of keyword arguments and print them in the format
key:value
# '''
# def print_kwargs(name,power):
#     print("Name ",name ," Power ",power)
#
# print_kwargs(name="Hammad",power="Knowledge")
# print_kwargs(power="Knowledge",name="Hammad")
# #agr named parameter hai to order matter nai krta
# '''
# agr mn chata hu assa ho ky jtni arrugment pass kryu utni hi aye ,new pass kryo vo bi add ho jaye
# to kuch krna hoga mujy'''

def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)
print_kwargs(name="Hammad",power="Knowledge")
print_kwargs(power="Knowledge")
print_kwargs(name="Hammad")
print_kwargs(name ="Hammad",power="Knowledge", section="BS.Cs")
