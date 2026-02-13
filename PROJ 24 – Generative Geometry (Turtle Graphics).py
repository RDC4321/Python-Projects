from turtle import Turtle, Screen
import random

gturtle = Turtle()
gturtle.shape("classic")
screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)


for sides in range(3,11):
    angle = 360/sides
    gturtle.speed(5)
    gturtle.pencolor(random_color())

    for i in range(sides):
        gturtle.forward(100)
        gturtle.left(angle)

screen.exitonclick()