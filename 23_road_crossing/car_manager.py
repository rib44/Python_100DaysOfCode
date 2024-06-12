from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SPEED = 0.8


class CarManager:

    def __init__(self):
        self.cars = []
        self.move_speed = 0.1

    def make_car(self):
        chance = randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.penup()
            random_y = randint(-250, 250)
            new_car.goto(300, random_y)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def has_collided(self, player):
        for car in self.cars:
            if car.distance(player) < 25:
                return True

    def car_cleanup(self):
        for car in self.cars:
            if car.xcor() < -330:
                del car

    def speedup(self):
        self.move_speed *= SPEED
