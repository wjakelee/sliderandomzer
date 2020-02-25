
from tkinter import *

window = Tk()
window.geometry('800x400')

window.title("Homepage")

top_frame = Frame(window).pack()
bottom_frame = Frame(window).pack(side = "bottom")

label = Label(window, text = "Please select an option below:").pack()

button_test = Button(top_frame, text = "Take Test", fg = "black", bg = "green").place(relx=0.4, rely=0.5, anchor=CENTER)

button_admin = Button(top_frame, text = "Setup, DataFile, Randomization (Admin Only)", fg = "black", bg = "blue").place(relx=0.6, rely=0.5, anchor=CENTER)

button_deskTop = Button(bottom_frame, text = "Exit to Desktop", fg = "black", bg = "red").place(relx=1.0, rely=1.0, anchor=SE)
window.mainloop()
