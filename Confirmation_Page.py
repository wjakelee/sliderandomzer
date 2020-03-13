from tkinter import *

window = Tk()
window.geometry('800x400')

window.title("Confirmation Page")
top_frame = Frame(window, background='white')
top_frame.place(anchor='nw', relwidth=1, relheight=1)

Label(top_frame, text = "Are You Sure You Want To End The Test?",font = 'Arial 20 bold', bg = "white").place(relx=0.5, rely=0.1, anchor = 'n')

Button(top_frame, text = "Yes", fg = "black", font = "Arial 14 bold", width = "25", height = "3",  bg = "#01DF3A").place(relx=.5, rely=.4, anchor=CENTER)

Button(top_frame, text = "No", fg = "black", font = "Arial 14 bold", width = "25", height = "3",  bg = "#FF0000").place(relx=.5, rely=.7, anchor=CENTER)



window.mainloop()