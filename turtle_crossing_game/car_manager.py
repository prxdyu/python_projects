from turtle import Turtle,Screen
from random import *
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

    

class CarManager:
    def __init__(self):
        self.list_of_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE
        
        
    def create_car(self):
        random_num=randint(1,8)
        if random_num==1:
            new_car=Turtle()
            new_car.hideturtle()
            new_car.penup()
            new_car.shape("square")
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_len=3,stretch_wid=1)
            new_car.setheading(180)
            random_y=randint(-250,250)
            new_car.goto(280,random_y)
            new_car.showturtle()
            self.list_of_cars.append(new_car)
            
    def move_cars(self):
        for i in self.list_of_cars:
            i.forward(self.car_speed)
            
    def level_up(self):
        self.car_speed+=MOVE_INCREMENT
        
        
        
   
        
        
        
