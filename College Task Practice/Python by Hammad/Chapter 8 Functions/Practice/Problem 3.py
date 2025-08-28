#4. Write a recursive function to calculate the sum of first n natural numbers.
'''
sum (n)=1+2+3+4+..+n
sum(1)=1
sum(2)=1+2
sum(3)=1+2+3
sum(4)=1+2+3+$
sum(n)=1+2+3+..n-1+n
sum(n)=n +sum(n-1)
'''
def sum(n):
    if (n==1) :
        return 1#base condition isliye lagaty hai ky infinite loop reverse mn na chaly
    return n+sum(n-1)
print(sum(5))