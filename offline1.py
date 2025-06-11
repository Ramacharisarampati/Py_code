'''
OOPS

Variable        variabl



'''



def function ():
    smiles=5
    print("function", smiles)

function()

class smiles:
    smile=5

print("class", smiles.smile)

class oops:
    def method(self):
        self.smile=5
        print("method", smiles.smile)

ram=oops()
ram.method()

def Fruit():

    fruit = "mango"
    quantity = 7
    rate = 12

    #Step 2: Variables

    fruit1 = fruit
    quantity1 = quantity

    #Step 3: Conditions

    if fruit == "mango":
        print ("Seasonal Fruit")

    if quantity == 7:
        Price = rate * quantity
        print ( "totla price " , Price)

    #Step 4: Loop

        times = 0
        while times<quantity:
            print ("packing")
            times = times+1

    #Print "Packing" 7 times using a while loop.

    #Step 5: Logic
    #Calculate weight if each mango weighs 250.75 grams.

    eachmango =250.75
    totalweight = eachmango*quantity

    print ("total weight is", totalweight)
Fruit()

class oops:

    def Fruit(self):

        self.fruit = "mango"
        self.quantity = 7
        self.rate = 12

        #Step 2: Variables

        self.fruit1 = self.fruit
        self.quantity1 = self.quantity

        #Step 3: Conditions

        if self.fruit == "mango":
            print ("Seasonal Fruit")

        if self.quantity == 7:
            Price = self.rate * self.quantity
            print ( "totla price " , Price)

        #Step 4: Loop

            times = 0
            while times<self.quantity:
                print ("packing")
                times = times+1

        #Print "Packing" 7 times using a while loop.

        #Step 5: Logic
        #Calculate weight if each mango weighs 250.75 grams.

        eachmango =250.75
        totalweight = eachmango*self.quantity

        print ("total weight is", totalweight)
rama=oops()
rama.Fruit()

#-------------------------------------------

class Mother:
    def calm_child(self):
        self.seetha ="toy"
        print (self.seetha)
ammo=Mother()
ammo.calm_child()
#--------------------------------------------

class Assignments:
    def assign_homework(self, age):
        if age < 6:
            self.draw = "drawing"
            print(self.draw)
        elif 6 <= age < 10:
            self.meth = "maths"
            print(self.meth)

object = Assignments()
object.assign_homework(5)
object.assign_homework(7)
#----------------------------------------------

class Birthday:
    wishlist = [{"toys":"heman"}, {"fav_color":"blue"}, {"playstation": "GTA_5"}]
    def distribute_gifts(self, wish):
        for i in Birthday.wishlist:
            if wish in i.keys():
                print ("Deam come true with", i[wish])
mybirthday = Birthday()
mybirthday.distribute_gifts("toys")
mybirthday.distribute_gifts("fav_color")
#-----------------------------------------------

def reusable():
    a=5
    print(a)
    return a

ret=reusable()
print(ret)

class reusable1:
    a=7

    def __init__(self):
        print ("init methods")
        self.variable =9
    def method(self):
        print (self.variable)
    def geeter(self):
        return self.variable

venkat = reusable1()
venkat.method()
ret=venkat.geeter()
print()
#-----------------------------------------------

#http://151.97.6.7

def reusable():
    a = 5
    print(a)
    return a


ret = reusable()
print(ret)


class reusable1:
    a = 7

    def __init__(self):
        print("init methods")
        self.variable = 9

    def method(self):
        print(self.variable)

    def geeter(self):
        return self.variable


venkat = reusable1()
venkat.method()
ret = venkat.method()
print(ret)