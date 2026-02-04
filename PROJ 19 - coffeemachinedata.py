MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0
is_on = True

while is_on:

    choice = input("what would you like? (espresso/latte/cappuccino):").lower()


    if choice == "off":
        is_on= False
    elif choice == "refill":
        resources["coffee"] = 100
        resources["water"] = 300
        resources["milk"] = 200
        print("Machine has been refilled successfully!")

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")

    elif choice in MENU:
        drink = MENU[choice]
        payment_success = False
        enough_resources = True
        for ingredient in drink["ingredients"]:
            if drink["ingredients"][ingredient] > resources[ingredient]:
                print(f"Sorry there is not enough {ingredient}.")
                enough_resources = False
                break
        if enough_resources:
            print(f"please insert coins: ")
            quarters = int(input("How many quarters: "))
            dimes = int(input("How many dimes: "))
            nickles = int(input("How many nickles: "))
            pennies = int(input("How many pennies: "))

            total = (quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01)
            cost = drink["cost"]
            print(f"Total inserted: ${total}")
            print(f"{choice} cost is ${cost}")
            
            if total < cost:
                print("Sorry that's not enough money. Money refunded!")
            else: 
                change = round(total - cost, 2)
                if change > 0:
                    print(f"here is ${change} dollars in change.")
                money += cost
                payment_success = True

            if enough_resources and payment_success:
                for ingredient in drink["ingredients"]:
                    resources[ingredient] -= drink["ingredients"][ingredient]
                print(f"here is your {choice}! Enjoy!")
    else: 
        print(f"Invalid selection")