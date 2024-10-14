#simple hangman project using while, if/elif, random, lists.
import random
#list containing the words to be guessed.
word_list=["python","program","code","computer","compile","megadeath"]
#blank list containing the letters user will input
correct_letters = []
#boolean variable that will be used for while loop.
game_over = False
#random function to choose which word to use.
chosen_word = random.choice(word_list)
#variable for players lives/chances
lives = 6

print("Let's play HANGMAN!")
print(f"The chosen word you have to guess is:")

#this is to display which word the player will guess at the start. 
display = ""
for display_loop in chosen_word:
    display += " _ "
print(display)

#while loop to keep repeating the program until all the words are guessed
while game_over != True:

    print(f"The number of lives you have is: {lives}")
    guess = input("Guess a Letter!: ").lower()
    #if module, that deducts 1 point from lives if the letter guessed is wrong and stay the same if letter guessed is correct
    if guess not in chosen_word:
        lives -=1
    else:
        lives +=0
#for loop to display the correct letters in the right position of the word & to keep unguessed and incorrect letters as "_"
    display2 = ""
    for game_loop in chosen_word:
        if game_loop == guess:
            display2 += game_loop
            correct_letters.append(guess)
        elif game_loop in correct_letters:
            display2 += game_loop
        else:
            display2 += " _ "
    print(display2)
#if statement for when all the "_" are gone, game_over will be turned to True, ending the while loop
    if "_" not in display2:
        print("You Win!")
        game_over = True
    elif lives == 0:
        print("You Lose!")
        game_over = True