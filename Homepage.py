
from tkinter import *

window = Tk()
window.geometry('800x400')

window.title("Homepage")

top_frame = Frame(window, background='white')
top_frame.place(anchor='nw', relwidth=1, relheight=1)


Label(top_frame, text = "Please select an option below:",font = 'Arial 20 bold', bg = "white").place(relx=0.5, rely=0.1, anchor = 'n')

Button(top_frame, text = "Take Test", fg = "black",font = 'Arial 14 bold', width = '9', height = '3', bg = "#33cc33").place(relx=0.355, rely=0.5, anchor=CENTER)

Button(top_frame, text = "Setup, DataFile,\nRandomization (Admin Only)", font = 'Arial 14 bold', width = '22', height = '3', fg = "black", bg = "#6699ff").place(relx=0.6, rely=0.5, anchor=CENTER)

Button(top_frame, text = "Exit to Desktop", fg = "black", bg = "#ff4d4d").place(relx=1.0, rely=1.0, anchor=SE)

window.mainloop()
