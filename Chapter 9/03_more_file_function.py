f=open("file.txt")

#lines =f.readlines()
#f.readlines jtni baar chalaye gyein utni baar lines read hoti jaye gi
line1=f.readlines()
print(line1,type(line1))

line2=f.readline()
print(line2,type(line2))

line3=f.readlines()
print(line3,type(line3))

line4 =f.readlines()
print(line4,type(line4))

f.close()