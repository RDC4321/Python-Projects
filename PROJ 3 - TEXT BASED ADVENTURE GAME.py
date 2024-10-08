#simple choose your own adventure project, if/elif project
print("Welcome to Treasure Island. Your mission is to find the treasure!")
choice1 = str(input("Choose which direction to go (LEFT/RIGHT): "))
if choice1 in ['left','Left','LEFT']:
        print("You go to the left path, as you walk you trip and fall into the river\n")
        choice2 = str(input("You sink and try you best to resurface, What will you do now? (SWIM/WAIT): "))
        if choice2 in ['wait','WAIT','Wait']:
            print("You take a few to catch you breath and composure. You then get swept by some violent magical current and pass out. \nYou wake up on a small island. You see a temple with 3 entrances.")
            choice3 = str(input("You go near the temple and see 3 different colored doors. \nWhich door will you open? (RED/YELLOW/BLUE): "))
            if choice3 in ['Red','red,','RED']:
                print("As soon as you open the red door, flames start sprouting from inside, burning you. Game Over")
            elif choice3 in ['Blue','BLUE','blue']:
                print("As soon as you open the blue door, beasts start jumping at you, tearing you limb from limb. Game Over")
            elif choice3 in ['Yellow','yellow','YELLOW']:
                print("As soon as you open the yellow door, an aura of calm envelopes you. it seems that you have found the treasure! You Win!!")
            else:
                print("You did not choose any of the doors, lightning strikes you from above. Smited by a powerful being. Game Over")
        else:
            print("You get attacked by monstrous sea creatures. Game Over")
else:
        print("You fell into a hole. Game Over")