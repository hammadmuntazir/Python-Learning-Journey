"""slicing refers to being able to extract certain parts of string
slicing work same way as taking subarrays for thr string
#[start,end+1,step]"""
str1=" Banana "
print(str1[2:5:2])
'''formatting refers to being able to manipulate  strings to format 
'''
print (str1.strip())#removes leading and trailing white spaces from a string
print(str1.replace("a","b"))#.replace(old,new) replace old value with new
str2="My name is Hammad"
print(str2.split("a",2)) #split string into array of substrings
#.join converts itterable into string
arr1=["My","Name","is"]
print ("".join(arr1))#it creates a string separating each item in list
# with whatever you have provided
name="Hammad"
print(f"Myname is {name}")
#f string allow you to put expresssion inside of string literals
