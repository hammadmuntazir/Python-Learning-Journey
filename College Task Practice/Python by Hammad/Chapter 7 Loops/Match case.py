'''x = int(input("Enter a number:"))
#x is the variable to match
match x:
    #if x is the variable to match
    case 0:
        print("x is zero")
    #Case with if-condition
    case 4:
        print("x is four")
    #Empty case with if-condition
    case _ if x!=90:  #use underscore for default case
        print(x,"is not 90")
    case _ if x!=80:
      print(x," is not 80")
    case _:
         print(x)
'''
x=input("Enter your name:")
match x:
    case"Hammad":
        print("Hello Hammmad")
    case "Ali":
        print("Hello Ali")
    case _ :#else condition by default
        print("name again")