#simple project to experiment with list methods & nested lists

fruits = ["Apple","Orange","Mango","Strawberries"]
vegetable = ["Brocolli","Potato","Lettuce","Cabbage"]
food = [fruits,vegetable]
print(food)

fruits.append(input("Add a fruit: "))
print(food)

vegetable.remove(input("Remove a veggie: "))
print(food)

print(food[0][0])
print(food[0][1])
print(food[0][2])

print(food[1][0])
print(food[1][1])
print(food[1][2])