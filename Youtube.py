class computer:
    def __init__(self):
        self.name = "Ram"
        self.age = 29


    def compare (self, other):
        if self.age == other.age:
            return True
        else:
            return False
c1 = computer()
c1.age = 30
c2 = computer()
#c1 and c2 both refering to variable called Ram, however, age update from 29 to 30 using self variable call.
if c1.compare(c2):
    print("Same age")
else:
    print("Different age")

print(c1.name)
print(c2.name)

#-----------------------------------------------

class car:
    wheels = 4
#"wheels" class variable, Variables that are shared among all instances of the class.
# They are defined at the class level (outside any method) and are the same for every object created from that class unless explicitly overridden.
# Class variables are declared directly in the class body.
    def __init__(self):
#instance variable, Variables that are unique to each instance of the class.
#They are defined inside the constructor (__init__) using the self keyword, which ensures that each object gets its own copy of the variable.
#Instance variables are declared inside the __init__ method (or other methods of the class using self).
        self.mil=10
        self.comp="BMW"

c1=car()
c2=car()

c1.mil=9
car.wheels=5

print(c1.comp, c1.mil, c1.wheels)
print(c2.comp, c2.mil, c2.wheels)
#----------------------------------------------