import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Road crossing")
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_up, key="Up")

game_is_on = True

while game_is_on:
    time.sleep(car.move_speed)
    screen.update()

    # write the scoreboard
    score.update_scoreboard()

    # create cars and get them moving
    car.make_car()
    car.move_cars()

    if car.has_collided(player):
        game_is_on = False
        score.game_over()

    # next level
    if player.finish_line():
        score.level_up()
        car.speedup()
        player.home_position()

    # car cleanup
    car.car_cleanup()

screen.exitonclick()
