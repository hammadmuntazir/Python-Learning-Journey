'''
Customize a cofee order :"Small","Medium",or"Large" with an option for
"Extra shot"of  espresso.
'''
order_size=input("Enter order size small ,medium ,large")
extra_shot=True#True kryu ga to condition apny ap true hojaye gi extra shot wali

if extra_shot:
    coffee =order_size +"Cofee with an extra shot"
else :
    coffee=order_size+"Cofee"
print("Order :",coffee)