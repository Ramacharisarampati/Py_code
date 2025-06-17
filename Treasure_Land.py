print("""
 .              +   .                .   . .     .  .
                   .                    .       .     *
  .       *                        . . . .  .   .  + .
            "You Are Here"            .   .  +  . . .
.                 |             .  .   .    .    . .
                  |           .     .     . +.    +  .
                 \|/            .       .   . .
        . .       V          .    * . . .  .  +   .
           +      .           .   .      +
                            .       . +  .+. .
  .                      .     . + .  . .     .      .
           .      .    .     . .   . . .        ! /
      *             .    . .  +    .  .       - O -
          .     .    .  +   . .  *  .       . / |
               . + .  .  .  .. +  .
.      .  .  .  *   .  *  . +..  .            *
 .      .   . .   .   .   . .  +   .    .            +
""")
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

# Room 1
room_1 = input("Which way would you like to go? Left or Right: ").lower()
if room_1 == "left":
    print("Right choice for Room 1!")
else:
    print("You fell into a hole. Game over!")
    exit()

# Room 2
room_2 = input("Now you have two options to win this round. "
               "Which task would you like to do? Jump or Swim: ").lower()
if room_2 == "swim":
    print("Right choice for Room 2!")
else:
    print("You got attacked by trout. Game over!")
    exit()

# Room 3
room_3 = input("Congratulations! You have reached Room 3.\nYou have three doors in front of you. "
               "Which one would you choose: Red, Blue, or Yellow? ").lower()
if room_3 == "red":
    print("Burned by fire. Game over!")
    exit()
elif room_3 == "blue":
    print("Eaten by beasts. Game over!")
    exit()
elif room_3 == "yellow":
    print("You Win!")
    exit()
else:
    print("Invalid choice. Game over!!!!!")
    exit()
    