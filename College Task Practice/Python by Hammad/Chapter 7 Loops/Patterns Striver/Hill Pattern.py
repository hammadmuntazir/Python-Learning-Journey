'''
          *
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * *
1)Decreasing space pattern
2)increasing star pattern
3)Increasing star pattern
but column is single so from 2 and 3 we have to print i increasing star pattern with
for i in range(i): and 2nd for i in range(i+1)

'''


n=5
for i in range(n):
    for j in range(i,n):
        print("-",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()