'''

print (type(True))
print (type("ABC"))
print (type(123))
print (type(1232.3))

print("hello world!\nhello world!")
print("HelloR " + input("What's your name?") +"!")

print(len(input("What's your name?")))

username = input("What's your name?")
lenght = len(username)
print(lenght)

glass1 = "milk"
glass2 = "juice"

temp = glass1
glass1 = glass2
glass2 = temp

print(glass1,'\n',glass2)
#-----------------------------------------------
print("welcome to the Band name generator")
city = input("What's your city?\n")
pet = input("What's your pet?\n")
print ("Your band name could be:", city +" "+ pet)
'''
# Day2

print ("Welcome to the tip calculator!")
total_bill = int(input("what is the total bill?\n"))
add_tip = int(input("How much tip would you like to give?\n"))
split_the_bill = float(input("How many people to split the bill?\n"))
convert = int(split_the_bill)
bill = add_tip+total_bill
print(bill)
print("Each person should pay: ", bill / convert)
#-----------------------------------------------
letters = len(input("Enter your name: "))
convert = str(letters)
print("Number of letters in your name: " + convert)

#-----------------------------------------------