'''A string is an array of single letters
'''
str1="banana"
print (str1[1])#elements accesed in strings are same as in array
'''For Captilizing every letter manually we would need a hash map
mapping every lower Case  letter to an upperCase  letter looping 
 through each letter in string and changing it to upper case letter
 '''
old_string="hammad"
new_string=""
hashmap={
    "h":"H",
    "a":"A",
    "m":"M",
    "m":"M",
    "a":"A",
    "d":"D"
}
for letter in old_string:
    new_string +=hashmap[letter]

print(new_string)
#it can done simply in python by using .upperCase
print(old_string.upper())