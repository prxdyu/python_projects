from random import *
from turtle import Screen,Turtle
from snake import *
from food import Food
from score import Score
import time
snake=Snake()
food=Food()
score=Score()
screen=Screen()
screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)
screen.setup(width=600,height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

game=True

#refer video for this part

while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
#detecting the collision
    
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()
        
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game=False
        score.game_over()
    
    for i in snake.turtles[1:]:
        if snake.head.distance(i)<0.5:
                game=False
                score.game_over()
if score.current_score>int(score.high_score):
    file=open("data.txt","w")
    file.write(str(score.current_score))
    file.close()
        
        
        
    
    
    
        
    
    
    
    
    
    
    


