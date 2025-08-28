              #Task 1: Reversing the String
name=input("Enter your name: ")
print("Orignal String =",name)
print("Reversed String =",name[::-1])

              #Task 2 Checking word is Palindrome or not
Word=input("Enter Word: ")
if Word==Word[::-1]:
    print("Your name is Palindrome")
else:
    print("Your name is not Palindrome")
               #Task 3 Series sum
num=int(input("Enter Number: "))
value=0
for i in range(1,num+1):
    value=value+i
print("Series Sum =",value)
              #Task 4 Password Verification
password=input("Enter Password: ")
if password=="cs-835":
    print("Password Verified")
else:
    print("Password Not Verified")