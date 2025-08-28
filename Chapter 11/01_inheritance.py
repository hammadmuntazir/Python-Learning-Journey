class Employee:
    company="ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"{self.name} is good with {self.Language} language")
a=Employee()
b=Programmer()
print(a.company,b.company)


  #assy coppy krky aik ky method child ko dena acha nai hai
# class Programmer:
#     company="ITC Infotech"
#     def show(self):
#          print(f"The name is {self.name} and the salary is {self.salary}")
#
#     def showLanguage(self):
#         print(f"{self.name} is good with {self.Language} language")

#Programmer class ko inherit kr raha hu employee sy,jo kuch employee mein tha
#vo sub kuch to programmer mein hai hi,baki aur cheezain main change or add krskta hu
#jo bi change krna hai sirf employee mein krna hoga baki sara jaga update ho jaye ga
