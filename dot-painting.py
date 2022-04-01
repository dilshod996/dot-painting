import turtle
from turtle import Turtle
import random

belly = Turtle()
turtle.colormode(255)

color_items = [(239, 236, 238), (238, 237, 236), (237, 237, 241), (26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]
belly.shape("arrow")
belly.penup()

belly.setheading(225)
belly.forward(300)
belly.setheading(0)

number_dots = 100
for x in range(1, number_dots):
    one_color = random.choice(color_items)
    belly.dot(20, one_color)
    belly.forward(50)

    if x % 10 == 0:
        belly.setheading(90)
        belly.forward(50)
        belly.setheading(180)
        belly.forward(500)
        belly.setheading(0)
turtle.exitonclick()