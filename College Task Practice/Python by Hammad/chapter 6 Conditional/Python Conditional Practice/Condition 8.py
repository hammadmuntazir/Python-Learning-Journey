'''
            Password Strength Checker
Check if a password is "Weak","Medium", or "Strong".Criteria <6chars (weak),6-10chars
(medium),>10Chars(strong)
'''
Password=input("Enter Password")
length =len(Password)
if length<6:
    print("Weak Password")
elif length<=10:
    print("Medium Password")
elif length>10:
    print("Strong Password")