# class Employee:#This is a class attribute
#     #name ="Hammad"
#     language ="Python"
#     salary = 10000
#
#     def __init__(self):# dunder method which is automatically called
#         print("I am creating an object")
#     def getInfo(self):
#         print(f"The language is {self.language}.The salary is {self.salary}")
#
#     @staticmethod
#     def greet():
#         print("Good Morning")
#     '''def greet(self):
#         print("Good Morning")
#     agr object self ka kaam nai to my static method use kryu ga
#     staticmethod sy humny isy function mark krdia hai
#     '''
# #for creating object
# hammad=Employee()#hammad is Object
# hammad.name ="Hammad"
# print(hammad.name,hammad.language,hammad.salary)
#
# Ali = Employee() # jub bi new object banaty hain __init__ dunder method call hota hai
# #init special method =>
# #method starting with double underscore(__) are known as dunder method in python


class Job:
    language ="Python"
    salary = 10000

    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating an object")

Hanan=Job("Hanan",13000,"Javascript")
print(Hanan.name,Hanan.salary,Hanan.language)