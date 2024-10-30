#simple program that simulates a number guessing game (alt # 1 - uses a single function for everything)
import random
from number_guess_resources import logo

def guessing_game():
    rnumber = random.randint(1,100)
    lives = 0
    game_over = False

    print(logo)
    print("Welcome to the random number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    #remove # below to show answer when running (for testing purposes)
    #print(rnumber)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty in ['easy','EASY','Easy']:
        lives = 10
    elif difficulty in ['hard','HARD','Hard']:
        lives = 5
    while game_over != True:
        print(f"You have {lives} attempts remaining to guess the number")
        user_guess = int(input("Guess a number: "))
        if user_guess == rnumber:
            game_over = True
            print(f"You got it! congrats! the answer was {user_guess}")
        elif user_guess > rnumber:
            print("Too High! Guess Again")
            lives -=1
        elif user_guess < rnumber:
            print("Too Low! Guess Again")
            lives -=1
        if lives == 0:
            game_over = True
            print("You've ran out of guesses and lost all your lives! Game Over!")


guessing_game()