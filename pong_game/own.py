from turtle import Screen,Turtle
from paddle import Paddle
screen=Screen()
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("Pong Game")
def r_paddle_up():
    r_paddle.goto(r_paddle.xcor(),r_paddle.ycor()+50)
def r_paddle_down():
    r_paddle.goto(r_paddle.xcor(),r_paddle.ycor()-50)
def l_paddle_up():
    l_paddle.goto(l_paddle.xcor(),l_paddle.ycor()+50)
def l_paddle_down():
    l_paddle.goto(l_paddle.xcor(),l_paddle.ycor()-50)
screen.listen()
screen.onkey(fun=r_paddle_up,key="Up")
screen.onkey(fun=r_paddle_down,key="Down")
screen.onkey(fun=l_paddle_up,key="w")
screen.onkey(fun=l_paddle_down,key="s")

