from tkinter import*
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep=0
timer=None
def start():
    global rep
    rep+=1
    work_sec=WORK_MIN*60
    break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if rep%2!=0:
        count_down(work_sec)
        label1.config(text="Work",fg=GREEN,bg=YELLOW,font=(FONT_NAME,25,"bold"))
    elif rep%2==0:
        count_down(break_sec)
        label1.config(text="Short Break",fg=PINK,bg=YELLOW,font=(FONT_NAME,25,"bold"))
    elif rep%8==0:
        count_down(long_break_sec)
        label1.config(text="Long Break",fg=GREEN,bg=RED,font=(FONT_NAME,25,"bold"))

def stop():
    window.after_cancel(timer)
    label_2.config(text="")
    label1.config(text="Timer")
    canvas.itemconfig(a,text="00:00")
    global rep
    rep=0

def count_down(count):
    min=int(count/60)
    sec=count%60
    if sec<10:
        sec=f"0{sec}"
    canvas.itemconfig(a,text=f"{min}:{sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start()
        check_makrs=""
        for _ in range(int(reps/2)):
            check_makrs+="✔"
        label_2.config(text=check_makrs)

window=Tk()
window.title("Pomodoro")
window.config(bg=YELLOW,padx=10,pady=10)

canvas=Canvas(height=250,width=250,bg=YELLOW,highlightthickness=0)#,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(125,125,image=tomato_img)
a=canvas.create_text(125,125,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(row=2,column=2)


label1=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,25,"bold"))
label1.grid(row=1,column=2)

button_start=Button(text="Start",width=5,command=start)
button_start.grid(row=3,column=1)

button_reset=Button(text="reset",width=5,command=stop)
button_reset.grid(row=3,column=3)

label_2=Label(bg=YELLOW,fg=GREEN)
label_2.grid(row=3,column=2)

window.mainloop()



# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #