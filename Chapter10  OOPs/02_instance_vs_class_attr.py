class Employee:#This is a class attribute
    #name ="Hammad"
    language ="Python"
    salary = 10000

#for creating object
hammad=Employee()#hammad is Object
hammad.language="JavaScript"#this is instance/object attribute
print(hammad.language,hammad.salary)
#instance attribute take preference over class attribute during
#assignment and retrieval