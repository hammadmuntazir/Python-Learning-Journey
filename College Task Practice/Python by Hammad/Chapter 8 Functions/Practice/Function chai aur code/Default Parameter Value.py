'''
Write a function that greets a user.
if no name is provided ,it should greet with default name.
'''
def greet(name="Hammad"):#Value di hai to value use ho jaye gi wrna apni jo kry gye vo hogi
    return "Hello ,"+name +"!"
print( greet())
print( greet("Ali"))