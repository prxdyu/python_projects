import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

tim=Player()
car=CarManager()
screen = Screen()
board=Scoreboard()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(key="Up",fun=tim.move)

game_is_on = True
while game_is_on:
    car.create_car()
    car.move_cars()
    # detection of collision with cars
    for i in car.list_of_cars:
        if tim.distance(i)<20:
            game_is_on=False
            board.game_over()
    # detection of turtle crossing the road
    if tim.ycor()>280:
        tim.reset_pos()
        car.level_up()
        board.increase_level()
        
    time.sleep(0.1)
    screen.update()
