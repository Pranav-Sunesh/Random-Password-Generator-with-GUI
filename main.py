from rand_password import random_password
from tkinter import *

def gen():
    max_length = entry1.get()
    special = x.get()
    obj = random_password(max_length, special)
    val = obj.generate()
    entry2.insert(0, val)
    entry1.config(state="readonly")
    button.config(state="disabled")
    reset_variable.set("Press reset for new value")
    
def reset():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry1.config(state="normal")
    button.config(state="normal")

def copy(event):
    clip_text=entry2.get()
    new.clipboard_clear()
    new.clipboard_append(clip_text)
    new.update()


new = Tk()
new.config(bg='#1E1E1E')
icon=PhotoImage(file="icon.png")
new.iconphoto(True,icon)
new.title("Password Generator")
new.geometry("500x90")
x = IntVar()
font_style = ("Courier New", 10, "bold")
reset_variable = StringVar()
label1 = Label(new, text="Minimum:", bg='#1E1E1E', fg='green', activebackground='#007F00', activeforeground='#00FF00', font=font_style)
label1.grid(row=0, column=0)
entry1 = Entry(new, bg='#2E2E2E', fg='green', insertbackground='green', font=font_style)
entry1.grid(row=0, column=1)
button = Button(new, text="Generate", command=gen, bg='#383838', fg='green', font=font_style, activebackground='#007F00', activeforeground='#00FF00')
button.grid(row=0, column=2)
label2 = Label(new, text="Charachters", bg='#1E1E1E', fg='green', activebackground='#007F00', activeforeground='#00FF00', font=font_style)
label2.grid(row=1, column=2)
check = Checkbutton(new, variable=x, bg='#1E1E1E', fg='green', activebackground='#007F00', activeforeground='#00FF00', font=font_style)
check.grid(row=1, column=3)
Label(new, text="Password:", bg='#1E1E1E', fg='green', activebackground='#007F00', activeforeground='#00FF00', font=font_style).grid(row=1, column=0)
entry2 = Entry(new, relief="raised", width="30", bg='#2E2E2E', fg='green', insertbackground='green', font=font_style)
entry2.grid(row=1, column=1)
repeat = Label(new, textvariable=reset_variable, bg='#1E1E1E', fg='green', activebackground='#007F00', activeforeground='#00FF00', font=font_style)
repeat.grid(row=2, column=1)
Button(new, text="reset", command=reset, bg='#383838', fg='green', font=font_style, activebackground='#007F00', activeforeground='#00FF00').grid(row=2, column=4)
new.bind("<Control-c>", copy)

new.mainloop()
