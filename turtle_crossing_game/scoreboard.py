from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.current_score=0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(-200,250)
        self.write(f"Level:{self.current_score}",align="center",font=FONT)
        
    def increase_level(self):
        self.current_score+=1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER !",align="center",font=FONT)
        
    
