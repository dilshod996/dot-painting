import turtle

import colorgram
import random
from turtle import Turtle

jenny = Turtle()

jenny.shape("arrow")
jenny.speed("fastest")

colors = colorgram.extract("hirst-image.jpg", 30)

turtle.colormode(255)


def color_list():
    all_colors = []

    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        all_colors.append(new_color)
    return all_colors


on_color = color_list()
print(on_color)
# for _ in range(5):
#     jenny.color(color_list())
#     jenny.forward(50)
#     jenny.right(90)




turtle.exitonclick()