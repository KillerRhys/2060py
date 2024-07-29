""" Desktop Todos Application
    Coded by TechGYQ
    www.mythosworks.com
    OC:2024.07.27(1558) """
import tkinter
# Imports
from tkinter import *
from logic import Logic
app = Logic()
app.load_data()

# GUI setting
display = Tk()
display.title("Tech's Todos")
display.minsize(width=800, height=800)
display.configure(bg='Black')

# Item label & settings
default_x = 0
default_y = 0
current_x = 0
current_y = 0
item = tkinter.StringVar()
item.set("Test")
item_label = tkinter.Label(display, textvariable=item, anchor=tkinter.CENTER, font=("Arial", 16, "bold"), bg="black", fg="red")
item_label.grid()

display.mainloop()
