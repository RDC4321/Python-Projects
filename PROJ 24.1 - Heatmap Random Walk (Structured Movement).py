from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

def color(distance):
    if distance > 500:
        distance = 500
    red = int((distance / 500) * 255)
    green = 255 - red
    blue = 0
    return (red,green,blue)

def direct(current):
    directions = [0,90,180,270]
    new_list = []
    opposite = (current + 180) % 360
    for direction in directions:
        if direction != opposite:
            new_list.append(direction)
    
    return new_list

gturtle = Turtle()
gturtle.shape("classic")
gturtle.speed("fastest")
gturtle.pensize(5)
gturtle.color("light green")

center_turtle = Turtle()
center_turtle.hideturtle()
center_turtle.penup()
center_turtle.goto(0,0)
center_turtle.dot()


for loop in range(500):
    current = gturtle.heading()
    allowed_direct = direct(current)
    gturtle.setheading(random.choice(allowed_direct))
    gturtle.forward(20)
    
    x_cord = gturtle.xcor()
    y_cord = gturtle.ycor()
    distance = (x_cord * x_cord + y_cord * y_cord) ** 0.5
    rgb = color(distance)
    gturtle.color(rgb)

center_turtle.goto(0,0)
center_turtle.dot()

screen.exitonclick()