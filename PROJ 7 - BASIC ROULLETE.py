#russian roullete/lottery project
#used random module, list/append, if/elif
import random
players=["Alex","Mark","Albert","Oppenheimer","Theodore"]
print("Welcome to our reverse SFW russian roullete minigame! Whoever get's chosen will receive $500,000,000!!!!")
play = str(input("Would you like to play? "))
if play in ['Yes','yes']:
    players.append(input("Very nice! What is your name? "))
    print(f"Welcome {players[5]}, take a seat. We'll start soon.")
    print(f"Ladies and Gents! meet our players!\n{players}")
    winner = random.choice(players)
    print(f"Let's start! our super lucky winner is: {winner}!!")
    print(f"Congrats {winner}!!")
elif play in ['No','no']:
    print("No problems! Enjoy the show")
    print(f"Ladies and Gents! meet our players!\n{players}")
    winner = random.choice(players)
    print(f"Let's start! our super lucky winner is: {winner}!!")
    print(f"Congrats {winner}!!")
else:
    print("Hmmm, that's not a yes or no. Good Bye!")
    