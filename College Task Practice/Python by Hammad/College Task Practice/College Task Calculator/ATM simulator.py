while True:

     pin=123
     balance=1000
     verifypin=int(input("Enter your pin:"));

     if(verifypin==pin):
         youwant=(input("Click 1 for check balance\n click2 for deposit "))
         if youwant==1:
             print("yourbalance is :",balance)
         elif youwant==2:
              print("you can deposit from ;",balance)

