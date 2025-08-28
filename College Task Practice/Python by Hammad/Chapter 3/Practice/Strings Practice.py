"""1. Write a python program to display a user entered name followed by Good
Afternoon using input () function.
"""
name=input("Enter your name:")
print(name,"Good Afternoon")
print(f"{name} Good Morning")#using variable in string but for it we should use "f" in start too

"""2. Write a program to fill in a letter template given below with name and date.
letter = ''' 
        Dear <|Name|>,
         You are selected!
        <|Date|>'''
"""
letter = ''' 
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>","Hammad").replace("<|Date|>","21/01/2025"))

#3. Write a program to detect double space in a string.
name="Hammad  is a good boy and"
print(name.find("  "))#Agr double space nai hogi to -1 aye ga

#4. Replace the double space from problem 3 with single spaces.
print(name.replace("  "," "))

