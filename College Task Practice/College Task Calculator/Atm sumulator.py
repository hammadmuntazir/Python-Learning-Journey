print("ATM sumulator")
a=int(input("press 1 to insert card : "))
if (a==1):
   b=int(input("Enter your pin : "))
psw=1122
while True:
   if (b==psw):
      print(" ")
      print("___________Welcome to ATM menu____________")
      break
   else:
      print("Invalid pin")
      b=int(input("Re-nter your pin : "))

while True:
      print(" ")
      print("Press 1 for Balance inquire")
      print("Press 2 for Cash deposit")
      print("Press 3 for Withdraw")
      print("Press 4 for Exit")
      print(" ")
      c=int(input("Enter your choice : "))
      inq=500000
      if c==1:
         print(" ")
         print("Welcome to balance inquire menu")
         print("Your current balance is : ",inq)
         print(" ")
      elif c==2:
         print(" ")
         print("Welcome to Cash deposit menu")
         d=int(input("Enter amount to deposit : "))
         inq=inq+d
         print("Your current balance is : ",inq)
         print(" ")
      elif c==3:
         print(" ")
         print("Welcome to Withdraw menu")
         e=int(input("Enter amount to withdraw : "))
         if e>inq:
            print("Insufficient balance")
         else:
            inq=inq-e
            print("Your current balance is : ",inq)
            print(" ")
      elif c==4:
         print(" ")
         print("Thank you for using ATM")
         print(" ")
         break
      else:
         print("Invalid choice")
                    