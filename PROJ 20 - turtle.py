from turtle import Turtle, Screen
import random

timmy = Turtle()
colors = ["red", "blue", "green", "orange", "purple", "cyan", "coral", "magenta", "pink", "yellow"]

sides = 7
angle = 360 / sides
print(timmy)
timmy.shape("turtle")
timmy.color("blue")
timmy.speed("fastest")
for turn in range(50):
    timmy.color(random.choice(colors))
    timmy.circle(100)
    timmy.left(10)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()