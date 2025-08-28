'''
5. Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*

'''
def pattern(n):
    if n==0:
        return# neechy wala call nai hoga idr return ka matlb hota hai function chal raha hai to baat khatam aggy nai chalna
    print("*"*n)
    pattern(n-1)
pattern(5)
# n=3
# for i in range(0,n):
#     print("*"*(n-i))