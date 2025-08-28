"""i=1
while (i<=50):
    print(i)
    i=i+1
"""
#Quick Quiz: Write a program to print the content of a list using while loops.
# l=[1,"Hammad","False",6,"Ali"]
# i=0
# while (i<len(l)):
#     print(l[i])
#     i=i+1
# print (len(l))#5

# for i in range(0,100,4):
#     print(i)

#for loop for list
l=[1,"Hammad","False",6,"Ali"]
for i in l:
    print(i)
#for tuple
t=(1,4,90.0)
for i in t:
    print(i)
#for string
s="hammad"
for i in s:
    print(i)
#for loop with else
l=[1,"Hammad","False",6,"Ali"]
for i in l:
    print(i)
else:
    print("The for loop is over")