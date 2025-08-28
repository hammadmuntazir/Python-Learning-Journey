'''
Choose a mode of transportation based on the distance (e.g.,<3km:Walk,3-15km:Bike,>15km:Car)
'''
distance= int(input("Enter distance"))
if distance <3:
    transport ="Walk"
elif distance<=15:
    transport="Bike"
elif distance>15:
    transport="Car"
print("You should use",transport ,"for",distance,"Km")