'''
          Pet Food Recommendation
Recommend a type of pet food based on the pet's species and age.(e.g.,Dog<2year-
Puppy food,Cat:>5year-Senior Cat food).
'''
name=input("Enter name of species Cat or Dog")
age=int(input("Age of Pet "))
if name == "cat" :
    if age <5 :
        print("Give it Junior Cat Food")
    elif age>=5:
        print("Give it Senior Cat Food")
elif name=="Dog":
    if age<2:
        print("Give it Puppy Food")
    elif age>=2:
        print("Give it Dog Food")