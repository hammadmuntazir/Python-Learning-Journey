'''
We all have played snake, water gun game in our childhood. If you haven’t, google the
rules of this game and write a python program capable of playing this game with the
user.

1 for  snake
-1 for water
0 for gun
'''

import random
computer =random.choice([-1,1,0])
youstr =input("Enter your choice: ")
youDict ={"s":1,"w":-1,"g":0}
reversedDict ={1:"snake",-1:"water",0:"gun"}
you=youDict[youstr]
#by now we have 2 numbers (variables),you and computer
print("Computer choose",reversedDict[computer],"\nYou choose",reversedDict[you])
if (computer==you):
    print("It's a tie!")

# else:
#     if(computer==-1 and you ==1):
#        print("You win!")#water drinked by snake
#
#     elif(computer==-1 and you ==0):
#        print("You lose!")#gun drown in water
#
#     elif(computer==1 and you ==-1):
#         print("You lose!")#computer snake you water
#
#     elif(computer==1 and you ==0):
#         print("You Win!")#snake ,gun
#
#     elif(computer==0 and you ==-1):
#          print("You Win!")#gun ,snake
#
#     elif(computer==1 and you ==0):
#          print("You Lose!")#snake,water
#
#     else:
#          print("something else")
if ((computer -you )==-1 or (computer -you)==2):
    print("You lose!")
else:
    print("You win!")