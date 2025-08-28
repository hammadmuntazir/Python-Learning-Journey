'''
                    Function with *args
Write a function that takes variable number of arguments and
returns their sum.
'''
#*args mean all arugments
#sum python ka default method jis mn ap jtny bi parameter dy skty ho aur pass krskty ho.
def sum_all(*args): #* lazmi hai baki args ki jaga kuch  bi likh skty hain
    print (args)
    for i in args:
        print(i**2)
    return sum(args)
print(sum_all(1,2,4))
#print(sum_all(1,2,3))
#print(sum_all(1,2,3,4,5,7))#mean jtny bi ho sub ka sum kro