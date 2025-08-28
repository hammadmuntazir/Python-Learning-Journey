'''
10. Write a program to print multiplication table of n using for loops in reversed
order
'''
#ya to list mn ly kr end pr list ko reverse krdo
n=int (input("Enter number:"))
for i in range(1,11):
   # print(f"{n} * {11-i} = {n*(11-i)}")
     print(n,"*",11-i,"=",n*(11-i))