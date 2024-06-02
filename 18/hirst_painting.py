# import colorgram
# colors = colorgram.extract("hirst_painting.jpg", 34)
# rgb_colors = []
# for c in colors:
#     color = (c.rgb.r, c.rgb.g, c.rgb.b)
#     rgb_colors.append(color)
#
# print(rgb_colors)

import random
import turtle

tim = turtle.Turtle()
tim.speed('fastest')
turtle.colormode(255)

color_list = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40),
              (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159),
              (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102),
              (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39),
              (164, 209, 187), (151, 206, 220), (97, 127, 168), (34, 81, 49), (180, 188, 210), (84, 65, 30)]


# variables
dot_diameter = 15
number_of_dots = 100

tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for dot_count in range(1, number_of_dots + 1):
    tim.pendown()
    tim.dot(dot_diameter, random.choice(color_list))
    tim.penup()
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

tim.ht()

screen = turtle.Screen()
screen.exitonclick()
