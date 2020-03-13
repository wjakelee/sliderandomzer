from tkinter import *

window = Tk()
window.geometry('800x400')

window.title("Test Intro Page")
top_frame = Frame(window, background='white')
top_frame.place(anchor='nw', relwidth=1, relheight=1)

Label(top_frame, text = "Please Enter The Following Information:",font = 'Arial 20 bold', bg = "white").place(relx=0.5, rely=0.1, anchor = 'n')

Label(window, text="Name:",fg = "black", background='white',font = 'Arial 12 bold').place(relx=0.38, rely=0.25, anchor=CENTER)
Label(window, text="Date:",fg = "black", background='white',font = 'Arial 12 bold').place(relx=0.38, rely=0.35, anchor=CENTER)
Label(window, text="Time:",fg = "black",background='white',font = 'Arial 12 bold').place(relx=0.38, rely=0.45, anchor=CENTER)
Button(top_frame, text = "Submit To Being The Test", fg = "black", bg = "#9FF781").place(relx=.5, rely=.6, anchor=CENTER)


e1 = Entry(window, background='light gray')
e2 = Entry(window, background='light gray')
e3 = Entry(window, background='light gray')

e1.place(relx=0.5, rely=0.25, anchor=CENTER)
e2.place(relx=0.5, rely=0.35, anchor=CENTER)
e3.place(relx=0.5, rely=0.45, anchor=CENTER)

Button(top_frame, text = "Back To Home", fg = "black", bg = "#81DAF5").place(relx=1.0, rely=1.0, anchor=SE)


window.mainloop()

