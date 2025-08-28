'''
Reverse string using loop
name=input("Enter string")
print(name[:: -1])'''
input =input("Enter string: ")
reversed_str=""

for char in input:
    reversed_str=char + reversed_str
print(reversed_str)