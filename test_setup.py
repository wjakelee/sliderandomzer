import tkinter as tk
from tkinter import *
import csv

set_wind = tk.Tk()
set_wind.title("Test Setup")     # window title
set_wind.geometry('800x480')
set_wind.configure(background='white')
frame = tk.Frame(set_wind, background='white')
canvas = tk.Canvas(frame, background='white')
scroll = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, background='white')

canvas.configure(scrollregion=(0, 0, 800, 7000))

canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
canvas.configure(yscrollcommand=scroll.set)

frame.place(anchor='nw', relwidth=1, relheight=1)
canvas.place(anchor='nw', relwidth=1, relheight=1)
scroll.pack(side='right', fill='y')

tk.Label(scrollable_frame, text="TEST SETUP", background='white', font='Arial 20 bold underline').grid(row=1, column=1)

tk.Label(scrollable_frame, text="\nCASE 1", background='white', font='Arial 12 underline').grid(row=2, column=1)
tk.Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=3, column=2)
tk.Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=3, column=3)
tk.Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=4, column=3)
tk.Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=5, column=3)

c1rt = StringVar()
c1he = StringVar()
c1nrc = StringVar()
c1ab = StringVar()
tk.Entry(scrollable_frame, textvariable=c1rt, background='#e6e6e6').grid(row=4, column=2)
tk.Entry(scrollable_frame, textvariable=c1he, background='#e6e6e6').grid(row=3, column=4)
tk.Entry(scrollable_frame, textvariable=c1nrc, background='#e6e6e6').grid(row=4, column=4)
tk.Entry(scrollable_frame, textvariable=c1ab, background='#e6e6e6').grid(row=5, column=4)


def entryData():
    a = c1rt.get()
    b = c1he.get()
    c = c1nrc.get()
    d = c1ab.get()
    print(a)
    print(b)
    print(c)
    print(d)


tk.Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=entryData).grid(row=4, column=1)

set_wind.mainloop()

# NEXT: SAVE ENTRIES TO DATA FILE (DETERMINE HOW I WANT TO FORMAT THE FILE) REPEAT THE CODE FOR 60 ENTIRES