'''
Create a recursive function to calculate recursion of a number
'''
#recursive is special technique of programming jis mn hum function ko wapis sy
#call krty rehaty hain program ky  andar hi
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

a=int(input("Enter a number: "))
print("The factorial of",a,"is",factorial(a))


#aksar log fikar krty hain recursion ki mgr humy krni hai recursion sy bahir annay ki
#kidr exit strategy hogi vo socho
#5 ka factorial ky liye boly ga 4 ka krlo
#4 ky factorial ky liye boly ga 3 ka pta krlo
#3 ky factorial ky liye boly ga 2 ka pta krlo
#2 ky liye boly ga 1 ka pata krlo
#1 ky liye boly ga 0 ka idr hogyi na problem aur is sy aggy bi
#isliye exite strategy lgani hogi