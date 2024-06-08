from turtle import Turtle
from random import randint

MOVE = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = MOVE
        self.y_move = MOVE
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # by upper and lower ball
        self.y_move *= -1

    def bounce_x(self):
        # by paddle
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.home()
        self.move_speed = 0.1
        self.bounce_x()

