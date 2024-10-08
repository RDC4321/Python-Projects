#simple rock paper scissor project.
#alternate way to build
#uses a single if/elif sequence instead of nested if/elif

import random
list = ["Rock", "Paper", "Scissors"]
print("Welcome to the Rock, Paper & Scissors game!!")
choice = str(input("Choose (Rock/Paper/Scissors): "))
ran=random.choice(list)
if choice in ['Rock'] and ran in ['Rock']:
    print(f"Draw! the AI chose {ran}")
elif choice in ['Rock'] and ran in ['Paper']:
    print(f"You Lose! the AI chose {ran}")
elif choice in ['Rock'] and ran in ['Scissors']:
    print(f"You Win! the AI chose {ran}")
elif choice in ['Paper'] and ran in ['Paper']:
    print(f"Draw! the AI chose {ran}")
elif choice in ['Paper'] and ran in ['Rock']:
    print(f"You Win! the AI chose {ran}")
elif choice in ['Paper'] and ran in ['Scissors']:
    print(f"You Lose! the AI chose {ran}")
elif choice in ['Scissors'] and ran in ['Scissors']:
    print(f"Draw! the AI chose {ran}")
elif choice in ['Scissors'] and ran in ['Paper']:
    print(f"You Win! the AI chose {ran}")
elif choice in ['Scissors'] and ran in ['Rock']:
    print(f"You Lose! the AI chose {ran}")
else:
    print("Error!!!!!")
