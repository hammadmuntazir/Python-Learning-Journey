'''
Write a generator function that yields even  number
upto a specified limit.
'''
#generator function generates value
def even_generator(limit):

     for i in range(                                                                                                                                                                            2,limit+1,2):
        yield i

for num in even_generator(12):
    print(num)
#yield  yaad rakhna hai value jo store hogyi usy