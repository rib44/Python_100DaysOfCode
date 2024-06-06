from turtle import Turtle, Screen


tim = Turtle()
# tim.shape("turtle")

# draw a box
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# draw a dashed line
# for _ in range(20_snakeGame):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# drawing different shapes
# import random as r
# distance = 100
# toggle = True
#
# for side in range(3, 11):
#     angle = 360 / side
#     color = (r.random(), r.random(), r.random())
#     tim.color(color)
#
#     toggle = not toggle
#     for _ in range(side):
#         tim.forward(distance)
#
#         if toggle:
#             tim.right(angle)
#         else:
#             tim.left(angle)

# draw a random walk
# import random
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
# distance = 30
# directions = [0, 90, 180, 270]
# tim.speed(8)
# tim.pensize(15)
#
# for _ in range(200):
#     tim.color(random.choice(colors))
#     tim.forward(distance)
#     tim.setheading(random.choice(directions))


# spirograph
import random as r

radius = 100
heading = 5
tim.speed("fastest")


def change_color():
    color = (r.random(), r.random(), r.random())
    tim.color(color)


for _ in range(round(360/heading)):
    change_color()
    tim.circle(radius)
    tim.setheading(tim.heading() + heading)

# footer
screen = Screen()
screen.exitonclick()
