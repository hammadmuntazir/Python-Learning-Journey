number_of_items=int(input("Number of items purchased :"))
rate=int(input("Enter rate of item:"))
total_price=number_of_items*rate
discount=total_price/10#10percent
if number_of_items>100:
    discounted_total_price=total_price-discount
    print(f'total price is {discounted_total_price}')
else:
    print(f'total price is {total_price}')
