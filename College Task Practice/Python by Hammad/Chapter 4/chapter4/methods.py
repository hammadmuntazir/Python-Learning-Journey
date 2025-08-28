from os import remove

friends =["Apple","Orange",5,345.06,"Ali","Muntazir"]

print(friends)

friends.append("Hammad")#print at end
print(friends)

#sort() -->arrange in ascending order
a=[1,4,5,18,0,20,2]
a.sort()
print(a)

#.reverse()-->reverses list
b=[1,4,5,18,0,20,2]
b.reverse()
print(b)

#insert(place where we want to insert,which is to insert )
c=[1,8,7,2,21,25]
c.insert(3,9)
print(c)

#pop
d=[1,4,5,6,7,8,9,0]
print(d.pop(3))

#remove()
d=[1,4,5,6,7,8,9,0]
d.remove(9)
print("d=",d)

