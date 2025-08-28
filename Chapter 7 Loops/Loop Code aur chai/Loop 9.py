'''
List uniqueness Checker
#Check if all elements in a list are unique .if a duplicate is found ,
exit the loop and print the duplicate.

# '''
# items = ["apple", "bannana", "orange", "apple", "mango"]
# for i in items:
#     if items.count(i)>1:
#         print("Duplicate found :",i)
#         break
items = ["apple", "bannana", "orange", "apple", "mango"]
unique_items=set()
for item in items:
    if item in unique_items:
        print("Duplicate found :",item)
        break
    unique_items.add(item)