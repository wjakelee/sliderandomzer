from tkinter import *

window = Tk()
window.geometry('800x400')

window.title("Randomization Selection")

top_frame = Frame(window, background='white')
top_frame.place(anchor='nw', relwidth=1, relheight=1)


Button(top_frame, text = "Test Setup", fg = "black",font = 'Arial 14 bold', width = '25', height = '3', bg = "#01DF3A").place(relx=0.5, rely=0.25, anchor=CENTER)

Button(top_frame, text = "Data File & Randomization", font = 'Arial 14 bold', width = '25', height = '3', fg = "black", bg = "#2E9AFE").place(relx=0.5, rely=0.5, anchor=CENTER)


Button(top_frame, text = "Back To Home", fg = "black", bg = "#81DAF5").place(relx=1.0, rely=1.0, anchor=SE)

window.mainloop()
