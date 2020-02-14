
from tkinter import *

window = Tk()
window.geometry('800x400')

window.title("Homepage")

top_frame = Frame(window).pack()
bottom_frame = Frame(window).pack(side = "bottom")

label = Label(window, text = "Please select an option below:").pack()

button_test = Button(top_frame, text = "Take Test", fg = "black").pack(side = "top")

button_admin = Button(top_frame, text = "Setup, DataFile, Randomization (Admin Only)", fg = "black").pack()

button_deskTop = Button(bottom_frame, text = "Exit to Desktop", fg = "black").pack(side = "right")

window.mainloop()
