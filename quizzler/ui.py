from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.minsize(width=450,height=500)
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.score_label=Label(text="Score:")
        self.score_label.config(bg=THEME_COLOR, fg="White", font=("Arial", 15,))
        self.score_label.grid(row=0, column=1)
        self.canvas=Canvas(height=300,width=400)
        self.canvas.grid(row=1,column=0,columnspan=2,padx=50,pady=50)
        self.question_text=self.canvas.create_text(200,150,width=260,text="Question",font=("Arial",20),fill=THEME_COLOR)
        true_image=PhotoImage(file=r"images\\true.png")
        self.true_button=Button(image=true_image,highlightthickness=0,command=self.true_pressed)
        self.true_button.grid(row=2,column=0)
        false_image = PhotoImage(file=r"images\\false.png")
        self.false_button = Button(image=false_image, highlightthickness=0,command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()
    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text,text=f"Quiz Ended ! you've Scored {self.quiz.score}/10")
    def true_pressed(self):
        is_right=self.quiz.check_answer("True")
        self.feedback(is_right)

    def false_pressed(self):
        is_right=self.quiz.check_answer("False")
        self.feedback(is_right)
    def feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)