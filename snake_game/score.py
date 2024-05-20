from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-200,y=270)
        self.current_score=0
        self.high_score=0
        self.color("yellow")
        self.update_scoreboard()
        self.show_highscore()
    
    def update_scoreboard(self):
         self.write(f"Score:{self.current_score}",False,align="center", font=('Arial', 15, 'normal'))
         self.show_highscore()
         

        
         
    def retrieve_highscore(self):
        file=open("data.txt")
        self.high_score=file.read()
         
         
    def show_highscore(self):
        self.goto(200,270)
        self.retrieve_highscore()
        self.write(f"High Score:{self.high_score}",False,align="center", font=('Arial', 15, 'normal'))
        self.goto(x=-200,y=270)
        
    
            
    def increase_highscore(self):
        pass
         
    
    
    def increase_score(self):
        self.current_score+=1
        self.clear()
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER !",False,align="center", font=('Arial', 20, 'normal'))
        
        
        
    