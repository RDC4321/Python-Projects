#Simple Rock Paper Scissors project
#utilizes random module, if/elif, & logical operators. 
import random
print("Head or Tails!")
coin=random.randint(1,2)
choose = int(input("Choose Heads(1) or Tails(2): "))
if coin==1 and choose==1:
    print("Heads, you win!")
elif coin==1 and choose==2:
    print("Heads, you lose!")
elif coin==2 and choose==2:
    print("Tails, you win!")
elif coin==2 and choose==1:
    print("Tails, you lose")
else: 
    print("Invalid Input! Death!")