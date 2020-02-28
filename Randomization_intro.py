from tkinter import *

window = Tk()
window.geometry('800x400')

window.title("Randomization Selection")

top_frame = Frame(window, background='white')
top_frame.place(anchor='nw', relwidth=1, relheight=1)


Button(top_frame, text = "Import Randomization Order", fg = "black",font = 'Arial 14 bold', width = '25', height = '3', bg = "#cc99ff").place(relx=0.5, rely=0.25, anchor=CENTER)

Button(top_frame, text = "Generate Randomization Order", font = 'Arial 14 bold', width = '25', height = '3', fg = "black", bg = "#ffcc66").place(relx=0.5, rely=0.5, anchor=CENTER)

Button(top_frame, text = "Export Data", font = 'Arial 14 bold', width = '25', height = '3', fg = "black", bg = "#99ff66").place(relx=0.5, rely=0.75, anchor=CENTER)

Button(top_frame, text = "Exit to Desktop", fg = "black", bg = "#ff4d4d").place(relx=1.0, rely=1.0, anchor=SE)

window.mainloop()
