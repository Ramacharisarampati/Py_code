'''
#Generator

def generator (variable):
    print ("generator", variable)
    yield 1
    print ("after yield")

obj=generator(5)
next(obj)
#next(obj)

#----------------------------------------

#Decorator

def decorator(variable):
    print("Ghost Protocol", variable)

    def hidden_function():
        print("hidden ghost", variable)
    return hidden_function

ret=decorator(7)
ret()
#-----------------------------------------
'''
#Advanced Decorator

def decorator(variable):
    print("Ghost Protocol", variable)

    def hidden_function():
        variable()
        print("hidden ghost", variable)
    return hidden_function

@decorator
def happy():
    print("happy")
happy()

