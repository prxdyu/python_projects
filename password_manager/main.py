from tkinter import*
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char
    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Password Manager",message="Please Make sure you haven't left any field empty")
    else:
        is_ok=messagebox.askokcancel(title="Password Manager",message=f"These are the details entered\nWebsite:{website}\nEmail:{email}\nPassword:{password}\n Is it ok to save?")
        if is_ok:
        #saving into the file
            file = open("data.txt", "a")
            file.write(f"\n{website} - {email} - {password}")
            file.close()
            #clearing the entries
            website_entry.delete(0,END)
            email_entry.delete(0,END)
            password_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.minsize(width=500,height=400)
window.config(padx=50,pady=50)

canvas=Canvas(height=200,width=200,highlightthickness=0)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

label_website=Label(text="Website:",pady=5)
label_website.grid(row=1,column=0)

label_email=Label(text="Email/Username:",pady=5)
label_email.grid(row=2,column=0)

label_password=Label(text="Password:",pady=7)
label_password.grid(row=3,column=0)

website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"pradyu1742@gmail.com")

password_entry=Entry(width=21)
password_entry.grid(row=3,column=1,)

generate_button=Button(text="Generate",width=10,command=generate_password)
generate_button.grid(row=3,column=2)

add_button=Button(text="Add",width=29,height=1,command=save)
add_button.grid(row=4,column=1,columnspan=2)






















window.mainloop()