from turtle import Turtle

FONT = ("Courier", 24, "normal")
POSITION = (-280, 260)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.pencolor("black")

    def update_scoreboard(self):
        self.clear()
        self.goto(POSITION)
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)

    def level_up(self):
        self.score += 1
