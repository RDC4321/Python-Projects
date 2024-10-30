#simple program that simulates a number guessing game (alt #2 - tried using multiple function for each vital parts. And I also made use of global constants)
import random
from number_guess_resources import logo

#global constants for the lives/turn amounts based on difficulty
HARD_LEVEL_LIVES = 5
EASY_LEVEL_LIVES = 10

def random_num():
    """function for generating the random number to be guessed"""
    rand_answer = random.randint(1,100)
    return rand_answer

def difficulty():
    """function for the lives that will be assigned based on difficulty chosen"""
    level = input("Choose difficulty, type 'Easy' or 'Hard': ")
    if level in ['easy','EASY','Easy']:
        return EASY_LEVEL_LIVES
    elif level in ['hard','HARD','Hard']:
        return HARD_LEVEL_LIVES
    else:
        return("Invalid Input!")

def check_guess(user_guess, answer, turns):
    """function for checking if user input is matching the number randomly chosen. it will return outputs based on various scenarios"""
    if user_guess == answer:
        print(f"Correct! The answer was {answer}! CONGRATS!")
    elif user_guess > answer:
        print("Too High!")
        return turns -1
    elif user_guess < answer:
        print("Too Low!")
        return turns -1

def game():
    """function for the entire program"""
    print(logo)
    answer = random_num()
    print("Welcome to the random number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    #remove # below to show answer when running (for testing purposes)
    #print(answer)
    turns = difficulty()   
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number!")
        guess = int(input("Make a guess: "))
        turns = check_guess(guess,answer,turns)
        if turns == 0:
            print(f"You've ran out of guesses! Game Over! The correct number was {answer}!")
            return
        elif guess != answer:
            print("Guess Again!")

game()