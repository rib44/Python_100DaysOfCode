from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(name="turtle")
        self.penup()
        self.setheading(90)
        self.home_position()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def home_position(self):
        self.goto(STARTING_POSITION)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
