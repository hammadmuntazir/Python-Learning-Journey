'''
7. Write a python function to remove a given word from a list and strip it at the same time.

'''
def rem(l,word):
    n=[]
    for item in l:
        if not (item==word):
            n.append(item.strip())
    return n
l=["Hammad","Ali",  "Hannan",  "Bilal"]

print(rem(l,"Bilal"))