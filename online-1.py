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

# Day2
#-----------------------------------------------
letters = len(input("Enter your name: "))
convert = str(letters)
print("Number of letters in your name: " + convert)

#-----------------------------------------------
height = 1.65
weight = 84

bmi = weight/(height**2)
print(bmi)
print(int(bmi))
#The round() function in Python rounds numbers to the nearest whole number or specified decimal places.
print(round(bmi))
print(round(bmi,2))
#-----------------------------------------------
#Assignment operators like +=, -=, and /= simplify updating variable values based on their current state.
score = 0
score = score + 1
print(score)
score += 1
print(score)
score -= 1
print(score)
score /=2
print(score)
score *=2
print(score)
#-----------------------------------------------
score = 100
height = 1.8
is_winning = True
#Using f-strings reduces manual conversion and concatenation, making code cleaner and easier to read.
#F-strings provide an efficient way to embed variables of different data types directly into strings without manual type conversion.
print(f"Your score is {score}, your height is {height}, your are winning is {is_winning}")
#-----------------------------------------------

print ("Welcome to the tip calculator!")
total_bill = float(input("what is the total bill?\n")) #float because bill can be 44.12
add_tip = int(input("How much tip would you like to give (in percentage)?\n"))
split_the_bill = int(input("How many people to split the bill?\n"))
bill = (total_bill * (add_tip / 100)) + total_bill
print("Bill including tip is =", bill)
split_amount = bill / split_the_bill
final_amout = round(split_amount, 2)
print(f"Each person should pay: {final_amout}")
#-----------------------------------------------
'''
#Day3
# Condition check

water_level = 90
if water_level > 80:
    print("Drain water")
else:
    print ("continue")
#-----------------------------------------------
print("Welcome to the rollercoaster!")
height = int(input("Whats is your height?\n"))
if height >= 150:
    print("You are allowed to ride rollercoaster")
if height == 120:
# one "=" sign means assigning value to variable.
# two "=" sing means check equality from left side to right side.
    print("You can ride mini rollercoaster")
else:
    print("You are not allowed to ride rollercoaster")