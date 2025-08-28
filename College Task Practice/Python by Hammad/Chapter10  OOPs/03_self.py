class Employee:#This is a class attribute
    #name ="Hammad"
    language ="Python"
    salary = 10000

    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")
    '''def greet(self):
        print("Good Morning")
    agr object self ka kaam nai to my static method use kryu ga
    staticmethod sy humny isy function mark krdia hai 
    '''
#for creating object
hammad=Employee()#hammad is Object
#hammad.language="JavaScript"#this is instance/object attribute
hammad.greet()
hammad.getInfo()
#=Employee.getinfo(hammad)#object pass into objectinfo

