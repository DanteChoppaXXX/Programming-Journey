#!./env/bin/python3
from tkinter import *
from time import *

def update():
    window.config(bg="#000000")
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    
    day_string = strftime("======\n%A\n======")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.title("Choppa Clock")
    window.after(1000,update)

window = Tk()

time_label = Label(window, font=("Times New Roman",50), fg="#ffffff", bg="#000000")
time_label.pack()

day_label = Label(window, font=("Cursive",25), fg="white", bg="#000000")
day_label.pack()

date_label = Label(window, font=("Times New Roman", 25), fg="white", bg="#000000")
date_label.pack()

update()

window.mainloop()