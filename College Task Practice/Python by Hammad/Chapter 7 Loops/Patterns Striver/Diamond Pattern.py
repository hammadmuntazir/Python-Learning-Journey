'''
-   - - - *
- - - - * * *
- - - * * * * *
- - * * * * * * *
* * * * * * * * * *
- * * * * * * * *
- - * * * * * * *
- - - * * * * *
- - - - * * *
- - - - - *

'''

''' 
n=5
for i in range(n-1):
    for j in range(i,n):
        print("-",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
vm    print()
for i in range(n):
      for j in range(i+1):
          print("-",end=" ")
      for j in range(i,n-1):
          print("*",end=" ")
      for j in range(i,n):
          print("*",end=" ")
print()
'''
"""n = 5  # Number of rows for the diamond pattern

# Upper part of the diamond
for i in range(n):
    for j in range(i, n - 1):
        print(" ", end=" ")  # Print spaces
    for j in range(i):
        print("*", end=" ")  # Print left stars
    for j in range(i + 1):
        print("*", end=" ")  # Print right stars
    print()

# Lower part of the diamond
for i in range(n - 1):
    for j in range(i + 1):
        print(" ", end=" ")  # Print spaces
    for j in range(i, n - 2):
        print("*", end=" ")  # Print left stars
    for j in range(i, n - 1):
        print("*", end=" ")  # Print right stars
    print()
"""
n=5
for i in range(n-1):#aik row kum ki hai
    for j in range(i,n):
        print("-",end=" ")
    for j  in range(i):#aik column kum kia hai increasing triangle pattren mn
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
#lower part
for i in range(n):
    for j in range(i+1):
        print("-",end=" ")
    for j in range(i,n-1):#aik column kum kia
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()