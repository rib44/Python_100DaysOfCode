from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_HEAD_POSITION = 0
ROTATION_ANGLE = 90


class Snake:
    def __init__(self):
        self.head = None
        self.segments = []
        self.create_snake()

    def create_snake(self):
        pos = STARTING_HEAD_POSITION
        for _ in range(3):
            head = Turtle(shape="square")
            head.color("white")
            head.penup()
            head.goto(pos, 0)
            self.segments.append(head)
            pos -= 20

        self.head = self.segments[0]

    def move(self):
        # first segment is not moved
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto((new_x, new_y))

        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        snake_direction = self.head.heading()

        if snake_direction == 0:
            # east facing
            self.segments[0].left(ROTATION_ANGLE)
        elif snake_direction == 180:
            # west facing
            self.segments[0].right(ROTATION_ANGLE)

    def down(self):
        snake_direction = self.head.heading()

        if snake_direction == 0:
            # east facing
            self.segments[0].right(ROTATION_ANGLE)
        elif snake_direction == 180:
            # west facing
            self.segments[0].left(ROTATION_ANGLE)

    def left(self):
        snake_direction = self.head.heading()

        if snake_direction == 90:
            # north facing
            self.segments[0].left(ROTATION_ANGLE)
        elif snake_direction == 270:
            # south facing
            self.segments[0].right(ROTATION_ANGLE)

    def right(self):
        snake_direction = self.head.heading()

        if snake_direction == 90:
            # east facing
            self.segments[0].right(ROTATION_ANGLE)
        elif snake_direction == 270:
            # west facing
            self.segments[0].left(ROTATION_ANGLE)
