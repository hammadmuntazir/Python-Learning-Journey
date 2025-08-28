#7. Write a program to find out whether a given post is talking about “Hammad” or not

post=input("Enter a post:")

if("Hammad".lower() in post.lower()):
    print("Yes, it is talking about Hammad")
else:
    print("No, it is not talking about Hammad")