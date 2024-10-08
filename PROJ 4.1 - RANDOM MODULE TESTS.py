#very simple test project, using random module.
#Here, instead of assigning a value ourselves for the ranges that the random module will use.
#the user will input ranges themselves.
import random
start = int(input("Choose starting number: "))
end = int(input("Choose ending number: "))
rng = random.randint(start,end)
print(rng)
