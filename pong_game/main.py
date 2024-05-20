from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time
screen=Screen()
score=Score()
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()
screen.onkey(fun=r_paddle.go_up,key="Up")
screen.onkey(fun=r_paddle.go_down,key="Down")
screen.onkey(fun=l_paddle.go_up,key="w")
screen.onkey(fun=l_paddle.go_down,key="s")

game=True

while game:
    time.sleep(ball.move_speed)
    ball.move()
    # detection with wall
    if ball.ycor() >280 or ball.ycor()<-280:
        ball.wall_bounce()
    # detection of collsion with paddle
    if (ball.distance(r_paddle)<30 and ball.xcor()>340) or (ball.distance(l_paddle)<30 and ball.xcor()<-340):
        ball.paddle_bounce()
    #detection of missing of right paddle
    if ball.xcor()>375:
        score.increase_l_point()
        time.sleep(1)
        ball.reset()
        ball.paddle_bounce()
    #detection of missing of left paddle    
    if ball.xcor()<-375:
        score.increase_r_point()
        time.sleep(1)
        ball.reset()
        ball.paddle_bounce()
        
    
    
    