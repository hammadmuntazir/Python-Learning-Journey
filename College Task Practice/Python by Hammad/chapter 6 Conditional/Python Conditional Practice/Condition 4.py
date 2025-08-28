'''
          Fruit Ripeness Checker
Determine if a fruit is ripe ,overripe or unripe based on its color(e.g.Banana :Green-unripe,Yellow-Ripe,Brown -Overipe
'''
# Banana={
#     "Green" :"Unripe",
#     "Yellow":"Ripe",
#     "Brown":"Overripe"
# }
# color =(input("Enter color of your Banana"))
# print(Banana[color])


#fruit ="Banana"
#color ="Yellow"
fruit=input("Enter Fruit name:")
color=input("Select Color of fruit from  Green,Yellow,Brown:")
if fruit =="Banana":
    if color=="Green":
        print("Unripe")
    elif color=="Yellow":
        print("Ripe")
    elif color=="Brown":
        print("Over-ripe")
