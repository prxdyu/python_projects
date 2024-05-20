from turtle import *
STARTING_POSITIONS=[(0,0),(-5,0),(-10,0)]
MOVE_DISTANCE=10
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    
    def __init__(self):
        self.turtles=[]
        self.create_snake()
        self.head=self.turtles[0]
        
    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_segment(i)
            
    def add_segment(self,position):
            segment=Turtle("square")
            segment.shapesize(stretch_len=0.5,stretch_wid=0.5)
            segment.color("white")
            segment.penup()
            segment.setpos(position)
            self.turtles.append(segment)
            
    def extend(self):
        self.add_segment(self.turtles[-1].pos())
    
    def move(self):
        for i in range(len(self.turtles)-1,0,-1):
            self.turtles[i].goto(self.turtles[i-1].pos())
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
        
        
        
            
