class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }
  
    def is_resource_sufficient(self,drink):
        for ingredient in drink.ingredients:
            if drink.ingredients [ingredient] > self.resources[ingredient]:
                print(f"Sorry, not enough {ingredient}.")
                return False
        return True
        
    def make_coffee (self, drink):
        for ingredient in drink.ingredients:
            self.resources[ingredient] -= drink.ingredients[ingredient]
        print(f"Here is your {drink.name}.")