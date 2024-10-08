#simple project that uses the random module.
#random numbers from ranges 1-10 will be generated each run, user will then input a number from the same range as well
#to see if the number matches.
import random
print("Test your luck with the number lottery!")
bet = int(input("Choose a number from (1-10): "))
print(f"Hmm, the number you've chosen is: {bet}!")
win = random.randint(1,10)
print(f"The winning number is: {win}")
if win==bet:
    print("You win!")
else:
    print("You lose!")