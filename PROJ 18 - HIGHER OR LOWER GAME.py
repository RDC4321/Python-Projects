import random
from higher_lower_data import data

def print_data(comp_data):
    """function that take the data and then returns it into printable format"""
    data_name = comp_data["name"]
    data_desc = comp_data["desc"]
    data_country = comp_data["country"]
    return f"{data_name}, {data_desc} from {data_country}"

def check_ans(guess, a_follower, b_follower):
    """function for checking if user guess is correct"""
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"

score = 0
playing = True
comp_b = random.choice(data)

print("WELCOME TO THE HIGHER / LOWER GUESSING GAME!\n")

while playing:
    comp_a = comp_b
    comp_b = random.choice(data)
    if comp_a == comp_b:
        comp_b = random.choice(data)

    print(f"Compare A: {print_data(comp_a)}.")
    print("Vs.")
    print(f"Against B: {print_data(comp_b)}.")

    guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()

    follower_a = comp_a['followers']
    follower_b = comp_b['followers']
    check_if_correct = check_ans(guess, follower_a,follower_b)

    if check_if_correct:
        score +=1
        print(f"\nYou are Right!, current score: {score}\n")
    else:
        print(f"\nYou are Wrong!, final score: {score}\n")
        playing = False