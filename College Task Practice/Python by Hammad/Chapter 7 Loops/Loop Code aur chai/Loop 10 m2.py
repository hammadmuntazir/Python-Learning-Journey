
from time import sleep
password=input("Enter password: ")
pswd="Hammad"

for check in range(1,6):
    if password==pswd:
        print("Access Granted")
        break
    else:
        print("Wrong Password")
        print("Attempt No:",check)
        sleep(check)
        password=input("Enter password: ")
        continue
else:
        print("Access Denied")

