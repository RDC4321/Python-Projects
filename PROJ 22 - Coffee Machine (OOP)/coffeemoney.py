class MoneyMachine:
    CURRENCY = "$"
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0

    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        print(f"Please insert coins. ")
        total = 0
        for coin in self.COIN_VALUES:
            total += int(input(f"how many {coin}?: ")) * self.COIN_VALUES[coin]
        return total
    
    def make_payment(self,cost):
        money_received = self.process_coins()
        if money_received < cost:
            print("sorry that's not enough money. Money refunded")
            return False

        change = round(money_received - cost, 2)
        if change > 0:
            print(f"here is {self.CURRENCY}{change} in change.")
        
        self.profit += cost
        return True