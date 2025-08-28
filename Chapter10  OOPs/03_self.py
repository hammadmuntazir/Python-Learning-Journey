# class Employee:#This is a class attribute
#     #name ="Hammad"
#     language ="Python"
#     salary = 10000

#     def getInfo(self):
#         print(f"The language is {self.language}.The salary is {self.salary}")

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
# #hammad.language="JavaScript"#this is instance/object attribute
# hammad.greet()
# hammad.getInfo()
# #=Employee.getinfo(hammad)#object pass into objectinfo

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# Ali=Person('Ali',25)
# print(Ali.name, Ali.age)

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def function(self):
#             print("This is a function inside a class")

# Ali=Person('Ali',25)
# Ali.age=40
# print(Ali.name, Ali.age)
# del Ali.age
# print(Ali.age)

class Person:
      def __init__(self,first_name,last_name):
         self.last_name=last_name
         self.first_name=first_name

      def printname(self):
           print(self.first_name,self.last_name)

class Student(Person):
    def __init__(self,first_name,last_name,student_id):
        super().__init__(first_name,last_name)  # Call the constructor of the parent class
        self.student_id = student_id

    def printname(self):
        print(f"Student Name: {self.first_name} {self.last_name}, ID: {self.student_id}")
X=Person('Hammad','Muntazir')
X.printname()