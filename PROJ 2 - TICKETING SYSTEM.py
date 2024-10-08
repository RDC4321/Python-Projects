#simple project simulating an online ticketing system utilizing if/elif to produce certain outputs based on different conditions
print("Welcome to the Coaster Roller Mega Ride!")
bill = 0
height = int(input("Requirement #1 - Please specify your height in CM: "))
if height>=120:
        print(f"Nice! You are {height}cm! you are elligible to ride the coaster roller!")
        age = int(input("Requirement #2 - Please specify your age: "))
        if age<12:
            print(f"Age:{age} - Tickets for kids are $5")
            bill=5
        elif age<=18:
            print(f"Age:{age} - Tickets for teens/youths are $7")
            bill=7
        elif age>=45 and age<=55:
            print(f"Age:{age} - Tickets are free $0 for people in the midlife crisis age range!")
        else:
            print(f"Age:{age} - Tickets for regular adults are $12")
            bill=12
        picture = str(input("Would you like to avail the photo package(+$2)? (Y/N): "))
        if picture in ['Y','y']:
            bill +=2
            print(f"Thank you for your time, the total bill will be: ${bill}")
        else: 
            print(f"Thank you for your time, the total bill will be: ${bill}")
else: print(f"Sorry! You are {height}cm, you need to be at least or over 120cm to ride the coaster roller.")