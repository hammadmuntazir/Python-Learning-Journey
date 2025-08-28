'''
Sum of Even Numbers:
Calculate the sum of even numbers up to given number n
'''

n=int(input("Enter number n"))
sum_even=0
for i in range(1,n+1):
    if i%2==0:

        sum_even+=i
print("Sum of even numbers is :",sum_even)