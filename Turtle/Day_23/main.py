import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

#instantiate classes
player = Player()
cars = CarManager()
scoreboard = Scoreboard()

# create player behaviour
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.level_number()

    # create car behaviour
    cars.create_car()
    cars.move()

    #detect new level (revert to beginning, start new level)
    if player.ycor() > 280:
        player.new_level()
        scoreboard.new_level()

    # detect collision
    for car in cars.all_cars:
        if car.distance(player) < 30:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()