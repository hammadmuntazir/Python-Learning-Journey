current_reading=int(input("Enter current reading of meter :"))
previous_reading=int(input("Enter previous reading of meter :"))
units=current_reading-previous_reading

surcharge=units*0.05/100

if units<300:
    bill=units*3.75
    print(f"Electricity bill is Rs.{bill} of {units}units")
elif units>300:
     bill=units*4.5+surcharge
     print(f"Electricity bill  is Rs.{bill} of {units}units")
