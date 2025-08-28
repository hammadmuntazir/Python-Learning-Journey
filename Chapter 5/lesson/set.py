d={}#empty dictionary
b=set()#empty set
print(type(b))
b.add(2)
b.add(3)
print(b)
b.remove(2)
print(b)

#set union
s1 ={1,45,6}
s2={7,8,1,78}
print(s1.union(s2))
print(s1.intersection(s2))