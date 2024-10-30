#simple program that simulates a blackjack game. it assumes that we have an infinite amount of deck. 
#makes use of previous knowledge such as functions, lists, random module, if/elif, for loop, while loop.
import random

def deal_card():
    """function that returns random card from the deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    dcard = random.choice(cards)
    return dcard

def calculate_score(cards):
    """function that takes the random cards returned as input then calculates the sum"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score,c_score):
    """function for comparing user & comp scores, then returning the result if win/lose/draw"""
    if u_score == c_score:
        return "Both scores are the same! It's a DRAW!"
    elif c_score == 0:
        return "Opponent got blackjack! You LOSE!"
    elif u_score == 0:
        return "You got blackjack! You WIN!!"
    elif u_score > 21:
        return "You went over 21! You LOSE!"
    elif c_score > 21:
        return "Opponent went over 21! You WIN!"
    elif u_score > c_score:
        return "You WIN!"
    else:
        return "You LOSE!"

def playblackjack():
    """function for the whole blackjack game"""
    user_cards = []
    computer_cards = []
    user_score = -1
    comp_score = -1
    game_over = False

    for loop1 in range (2):
        #loop for the cards that are dealt to user & comp at the beginning of the game
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while game_over != True:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(computer_cards)

        print(f"Your cards are: {user_cards}, your current score is: {user_score}")
        print(f"The computer's first card is: {computer_cards[0]}")
        
        choice = input("Would you like to draw another card? type 'Y' if yes, type 'N' if no: ")
        if choice in ['y','Y']:
            user_cards.append(deal_card())
        elif choice in ['n','N']:
            game_over = True
        else:
            game_over = True
            print("Invalid Input! Game Over!")

    while comp_score != 0 and comp_score < 17:
        #while loop for the opponent side to draw cards if current score is less than 17.
        computer_cards.append(deal_card())
        comp_score = calculate_score(computer_cards)

    print(f"Your final cards are: {user_cards}, your final score is: {user_score}")
    print(f"Your opponent's final cards are: {computer_cards}, your opponent's final score is: {comp_score}")
    print(compare(user_score,comp_score))

while input("Do you want to play Blackjack? type 'Y' if yes, 'N' if no: ") in ['Y','y']:
    print("\n" * 20)
    playblackjack()