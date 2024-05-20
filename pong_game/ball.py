from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.penup()
        self.color("red")
        self.goto(0,0)
        self.x_move=10
        self.y_move=10
        self.move_speed=0.1
    
    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)
    
    def wall_bounce(self):
        self.y_move*=-1
        
    def paddle_bounce(self):
        self.x_move*=-1
        self.move_speed*=0.09
    
    def reset(self):
        self.hideturtle()
        self.goto(0,0)
        self.showturtle()
        self.move_speed=0.1
        
    
        
        