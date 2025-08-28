"""name="Hammad"
nameshort =name[0:3]#start from index 0  all the way till 3 (excluding 3)
print(nameshort)
character1=name[1]
print(character1)
"""
a="0123456789"
print(a[1:8:3]) #"mean 1 to 8(mean 0 to 7 ky hissab sy 7 aye ga) tak value ko pahly  ly lain gye usky baad us value mn sy 2 ko skip krky 3rd likhy gye"

  #Functions of String
name ="hammad"
print(len(name))#string ki length deta hai
print(name.startswith("mad"))
print(name.endswith("mad"))
print(name.upper())#make string to uppercase
print(name.lower())#make string to lowercase
print(name.count("m"))#count number of occurrences
print(name.capitalize())#capatilize first letter
print(name.find("d"))#find index of word
print(name.replace("a","c"))

  #Escape Sequences
c=("Hammad is a good \n but not a \"bad\" b\\""34 oy")
print(c)