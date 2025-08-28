# *args taking all arguments as tuple
# *kwargs taking all arguments as dictionary

def greet(fx):
    def mfx(*args,**kwargs):
        print('Good Morning')
        fx(*args,**kwargs)
        print('Thanks for using this function')
    return mfx

@greet
def add(a,b):
    print(a+b)

greet(add)(1,2)