#Basic Method of creating class and object
class Employee:#This is a class attribute
    #name ="Hammad"
    language ="Python"
    salary = 10000

#for creating object
hammad=Employee()#hammad is Object
hammad.name="Hammad"#this is instance/object attribute
print(hammad.name,hammad.language,hammad.salary)

ali=Employee()
ali.name="Ali"
print(ali.name,ali.language,ali.salary)

'''
Here name is object/instance attribute
salary and language are class attribute as they directly belong to class
'''