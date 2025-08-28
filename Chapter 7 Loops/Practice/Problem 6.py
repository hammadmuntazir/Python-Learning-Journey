#6. Write a program to calculate the factorial of a given number using for loop.
#5!=1*2*3*4*5  1 sy us number tak multiply
n =int(input("Enter a number: "))
product =1 #sum mn zero sy intialize krty hai aur product mn 1 sy
for i in range(1,n+1):#n wesy to n-1 hota hai range mn mgr humy us number tak jana hai n+1 hoga isliye
     product=product*i
print("Factorial of",n,"is",product)
