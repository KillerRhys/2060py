""" Desktop Todos Application
    Coded by TechGYQ
    www.mythosworks.com
    OC:2024.07.27(1558) """

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


display.mainloop()
