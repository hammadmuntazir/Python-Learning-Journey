class Person:
    def __init__(self,name,age):
        self.name= name
        self.age=age
    
    def introduce(self):
        print(f'Hello,my name is {self.name} and i am {self.age} years old.')

class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id=student_id

    def introduce(self):
           print(f'Hello,my name is {self.name}, I am {self.age} years old and my student ID is {self.student_id}.')


Ali=Student('Ali', 20, 'S12345')
Ali.introduce()