'''
Add a method to the Car class that displays the full  name of
the car (brand and model)
'''
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def full_name(self):#full name mein bi connection line banana zarori hai warna hum variable tak nai ponch paye gyein
        return f"{self.brand} {self.model}"#class ky andar telephone line sy hi bulaya jata hai


mycar1 =Car("Honda","City")
print(mycar1.brand)
print(mycar1.model)
print(mycar1.full_name())#full name function hai isliye() jubky brand and model are variable


mycar2 =Car("CD","70")
print(mycar2.brand)
print(mycar2.model)
print(mycar2.full_name())