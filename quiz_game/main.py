import turtle
import pandas as p
screen=turtle.Screen()
tim=turtle.Turtle()
screen.title("USA Game")
img="blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
lst_states=[]


"""with open("50_states.csv","r")as f:
    reader=csv.reader(f)
    for coloumn in reader:
        x_y = []
        lst_states.append(coloumn[0])
        x_y.append(coloumn[1])
        x_y.append(coloumn[2])
        lst_positions.append(x_y)"""

answered=0
while answered!=50:

    user_answer=screen.textinput(title=f"{answered}/50 states correct",prompt="Guess one of the state")
    user_answer=user_answer.title()
    data = p.read_csv("50_states.csv")
    lst_states = data["state"].to_list()
    if user_answer in lst_states:
        answered+=1
        tim.hideturtle()
        tim.penup()
        state_data=data[data["state"]==user_answer]
        tim.goto(int(state_data.x),int(state_data.y))
        tim.write(user_answer)



















turtle.mainloop()