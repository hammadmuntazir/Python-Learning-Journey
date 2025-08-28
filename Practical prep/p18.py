basic_pay=int(input("Enter basic pay :"))
#rent
rent=basic_pay*35/100
#medical
if basic_pay>5000:
    medical=basic_pay*5/100
    conveyance =2000
else:
    medical=basic_pay*7/100
    conveyance = 1500

net_pay=basic_pay+medical+conveyance+rent
print(f"Net Pay is = {net_pay}")