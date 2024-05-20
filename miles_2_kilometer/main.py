from tkinter import*
def clicked():
    val=float(input.get())*1.6
    label3.config(text=round(val,2))
window=Tk()
window.title("Mile to km converter")
window.minsize(width=200,height=100)
window.config(padx=10,pady=10)
input=Entry(width=10)
input.grid(row=1,column=2)
label1=Label(text="Miles")
label1.grid(row=1,column=3)
label2=Label(text="is equal to")
label2.grid(row=2,column=1)
label3=Label()
label3.grid(row=2,column=2)
label4=Label(text="Kilometers")
label4.grid(row=2,column=3)
button=Button(text="Calculate",command=clicked)
button.grid(row=3,column=2)










window.mainloop()