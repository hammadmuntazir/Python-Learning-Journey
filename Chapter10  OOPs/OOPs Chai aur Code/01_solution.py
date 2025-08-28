'''
Create a Car class with attribute like brand and Model.Then create an instance of this class
'''
class Car:
    def __init__(self,brand,model):
        self.brand=brand#variable=parameter
        self.model=model

mycar =Car("Mehran","Suzuki")
print(mycar.brand)
print(mycar.model)

mycar2=Car("Tata","Safari")
print(mycar2.brand)
print(mycar2.model)

