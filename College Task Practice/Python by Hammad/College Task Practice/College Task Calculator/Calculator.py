def calculator():
      while True:
           print('''Calculator by Hammad ,Fazal and Mazhar
                    enter 1 for Addition 
                    enter 2 for subtraction
                     enter 3 for multiplication
                     enter 4 for divison
                     enter yes if you wanna end function''')
           a=int(input("Enter 1st number:"))
           b=int(input("Enter 2nd number :"))
           operation=int(input("Enter number according to operation you want"))
           if(operation==1):
               print(a+b)
           elif(operation==2):
               print(a-b)
           elif(operation==3):
               print(a*b)
           elif(operation==4):
               if(b==0):
                   print("Enter non zero number")
               else:
                   print(a/b)
           wannaend=input("enter yes for exit ")
           if wannaend=="yes":
               break

calculator()