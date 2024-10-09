#simple program that simulates dice rolls. Uses loops and random
#user inputs how many times to roll
#computer rolls the dice until = to user input
#while rolling, computer tracks how many times it has rolled a 6, and then prints it out for the user.
import random
print("Dice roller")
throw = 0
sixes = 0
roll = int(input("How many times will you roll the dice? "))
for loop in range(0,roll):
    throw += 1
    dice = random.randint(1,6)
    print(f"You rolled a {dice}")
    if dice == 6:
        sixes += 1
print(f"You rolled a '6' {sixes} times!")