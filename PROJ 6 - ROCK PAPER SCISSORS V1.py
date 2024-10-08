#simple rock paper scissors project
#used random module + lists + nested ifs/elif
import random
choice = input("Enter a choice (rock, paper, scissors): ")
list = ["paper","rock","scissors"]
ran = random.choice(list)
if choice == ran:
    print(f"Both players selected {choice}. It's a tie!")
elif choice == "rock":
    if ran == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif choice == "paper":
    if ran == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif choice == "scissors":
    if ran == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")