from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the colour: ").lower()

start_x = -230
start_y = 130

turtle_list = []

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=start_x, y=start_y)
    turtle_list.append(new_turtle)
    start_y -= 50

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} turtle is the winner.")
            else:
                print(f"You've lost The {winning_turtle} turtle is the winner.")
            break
        r_distance = random.randint(0, 10)
        turtle.forward(r_distance)

screen.exitonclick()
