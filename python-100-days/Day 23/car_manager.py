import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
SPEED_INCREASING = 5

from turtle import Turtle

class CarManager:
    def __init__(self, player):
        self.cars = []
        self.player = player
        self.game_on = True
        self.cars_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)

        if random_chance == 1:
            car = Turtle('square')
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setpos(x=310 + (random.randint(100, 500)), y=random.randint(-250, 250))
            time.sleep(random.randint(0, 1)/1000)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.cars_speed)
            if car.xcor() < -300:
                car.setpos(x=310 + (random.randint(100, 500)), y=random.randint(-250, 250))
            self.car_touch_player(car)

    def car_touch_player(self, car):
        is_collided = abs(self.player.xcor() - car.xcor()) < 30 and abs(
            self.player.ycor() - car.ycor()) < 20

        if is_collided:
            self.game_on = False

    def increase_speed(self):
        self.cars_speed += SPEED_INCREASING
