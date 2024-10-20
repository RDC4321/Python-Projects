#SIMPLE PROGRAM THAT SIMULATES AN AUCTION
#it takes user's name and amount of bid, which the program stores into an empty dictionary
#the for loop + if will then go through the dictionary to find the key & value with the highest amount.


bids = {}
end = False

print("Welcome to the secret auction program!")

while end != True:
    name = input("What is your name? ")
    bidding = int(input("How much will you bid? $"))
    bids[name]=bidding
    choice = input("Are there any other bidders? Type 'yes' or 'no': ")
    if choice == 'no':
        end = True
    elif choice == 'yes':
        end = False
    else:
        end = True
        print("Invalid Input!")

highest_bid = 0
for loop1 in bids:
    bid_amount = bids[loop1]
    if bid_amount> highest_bid:
        highest_bid = bid_amount
        winner = loop1
    #highest_bid = max(bids.values())
    
#print(bids)
print(f"The winner of this auction is {winner}! with a bidding amount of ${highest_bid}")