import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager(player)
score = ScoreBoard(-250, 250)

screen.listen()
screen.onkey(player.move_up, 'w')
screen.onkey(player.move_down, 's')

while car_manager.game_on:
    time.sleep(0.08)

    car_manager.move_cars()
    if player.ycor() > 290:
        player.move_to_start()
        car_manager.increase_speed()
        score.increase_score()

    screen.update()
    car_manager.create_car()

score.game_over()
screen.exitonclick()
