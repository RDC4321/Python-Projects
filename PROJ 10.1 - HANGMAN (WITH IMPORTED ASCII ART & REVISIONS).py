import random
from hangman_resources import word_list, hangman_logo, hangman_stage

correct_letters = []
game_over = False
chosen_word = random.choice(word_list)

lives = 6

print(hangman_logo)
print("Let's play HANGMAN!")
print(f"The chosen word you have to guess is:")


display = ""
for display_loop in chosen_word:
    display += " _ "
print(display)


while game_over != True:
    
    print(f"The number of lives you have is: {lives}/6")
    guess = input("Guess a Letter!: ").lower()
    if guess not in chosen_word:
        lives -=1
        print(f"You guessed '{guess}', which is incorrect, you LOSE a life!")
    else:
        lives +=0
        print(f"You guessed '{guess}', which is correct, you KEEP your life!")
    if guess in correct_letters:
        print(f"You already guessed the letter {guess}, no life will be reduced")
        
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
    
    if "_" not in display2:
        print("You Win!")
        game_over = True
    elif lives == 0:
        print("You Lose!")
        print(f"The word you had to guess is: {chosen_word}")
        game_over = True
    print(hangman_stage[lives])