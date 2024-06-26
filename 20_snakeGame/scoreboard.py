from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open("data.txt", "w") as wr:
                wr.write(f"{self.high_score}")

        self.score = 0
        self.update_score()

    def update_score(self, point=1):
        self.score += point
        self.print_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
