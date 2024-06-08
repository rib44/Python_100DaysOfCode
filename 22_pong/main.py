import time
from ball import Ball
from turtle import Screen, Turtle
from paddle import Paddle
from scoreboard import Scoreboard

HEIGHT = 600
WIDTH = 800
L_PADDLE = (-350, 0)
R_PADDLE = (350, 0)

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)    # turns off the animation of turtle

ball = Ball()
dash = Turtle()
paddle_left = Paddle(L_PADDLE)
paddle_right = Paddle(R_PADDLE)
scoreboard = Scoreboard()

# draw the middle line
dash.pencolor("white")
dash.hideturtle()
dash.pensize(4)
dash.penup()
dash.goto(0, -(HEIGHT/2 - 10))
dash.left(90)

while dash.ycor() < (HEIGHT / 2):
    dash.pendown()
    dash.forward(15)
    dash.penup()
    dash.forward(15)

screen.listen()
screen.onkey(fun=paddle_right.up, key="Up")
screen.onkey(fun=paddle_right.down, key="Down")
screen.onkey(fun=paddle_left.up, key="w")
screen.onkey(fun=paddle_left.down, key="s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    # detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with both paddles
    if ((ball.distance(paddle_right) < 50 and ball.xcor() > 320) or
            (ball.distance(paddle_left) < 50 and ball.xcor() < -320)):
        ball.bounce_x()

    # detect R paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect L paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
