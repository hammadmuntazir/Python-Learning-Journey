'''
for n=3
  *
 ***
*****  #outer loop is for printing rows matlb n rows hogi
'''
n=int(input("Enter a number: "))
for i in range(1,n+1):#bcz number tak krvani hai print
     print(" "*(n-i),end="")#number sy aik space kum chyiea
     print("*"*(2*i-1),end="") #odd ki series ky liye 2n-1
     print()