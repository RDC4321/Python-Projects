#Simple Python project simulating ordering pizza online
#S = 15$
#M = 20$
#L = 25$
#adding pepperoni = +2$ if small ; +3$ if medium/large
#adding chese = +1$ for all sizes
print("Welcome to Joe's Pizza Pizzaria!")
bill=0
size = str(input("What size pizza do you want? (S/M/L): "))
if size in ['S','s']:
    bill +=15
elif size in ['M','m']:
    bill +=20
elif size in ['L','l']:
    bill +=25
else:
    print("Invalid input. Choices are (S/M/L) only")
pepperoni = str(input("Do you want additional pepperonis on your pizza? (Y/N)"))
if pepperoni in ['Y','y']:
    if size in ['S','s']:
        bill+=2
    else: bill+=3
else:
    bill+0
cheese = str(input("Do you want extra cheese on your pizza? (Y/N): "))
if cheese in ['Y','y']:
    bill+=1
else:
    bill+0
print(f"The total bill is ${bill}!")