from turtle import *
from random import *
race=False
screen=Screen()
screen.setup(height=500,width=500)
user_bet=screen.textinput(title="Welcome to Turtle Racing Championship ",prompt="Who will win the race ? Bet on a color :")
turtles=["red","blue","green","yellow","purple"]
colors=["red","blue","green","yellow","purple"]
y_pos=-100
x_pos=-230
for i in range(0,5):
    
    turtles[i]=Turtle(shape="turtle")
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x=x_pos,y=y_pos)
    y_pos+=50

if user_bet:
    race=True

while race:
    for j in turtles:
        if j.xcor()>230:
            race=False
            winning_color=j.pencolor()
            if winning_color==user_bet:
                print(f"You Won The {winning_color} turtle is the winner")
            else:
                print(f"You Lost the {winning_color} turtle is the winner")
        
        random_num=randint(0,10)
        j.forward(random_num)