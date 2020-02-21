from tkinter import *
import csv


set_wind = Tk()
set_wind.title("Test Setup")                    # window title
set_wind.geometry('800x480')                    # window geometry
set_wind.configure(background='white')
frame = Frame(set_wind, background='white')
canvas = Canvas(frame, background='white')
scroll = Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas, background='white')

canvas.configure(scrollregion=(0, 0, 800, 7000))        # window scroll length

canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
canvas.configure(yscrollcommand=scroll.set)             # set canvas to scroll

frame.place(anchor='nw', relwidth=1, relheight=1)       # Frame placement
canvas.place(anchor='nw', relwidth=1, relheight=1)      # canvas placement
scroll.pack(side='right', fill='y')                     # scroll bar placement

Label(scrollable_frame, text="TEST SETUP", background='white', font='Arial 20 bold underline').grid(row=1, column=1)


fields = ['Case', 'Reagent Type', 'h&e Slide', 'Nrc Slide', 'Ab Slide']
with open('case_information.csv', 'w') as caseinfo_csv:
    csv_writer = csv.writer(caseinfo_csv)
    csv_writer.writerow(fields)


# ----- Begin case 1 Entry

Label(scrollable_frame, text="\nCASE 1", background='white', font='Arial 12 underline').grid(row=2, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=3, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=3, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=4, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=5, column=3)

c1rt = StringVar()      # change variable type to string for user entry
c1he = StringVar()
c1nrc = StringVar()
c1ab = StringVar()
Entry(scrollable_frame, textvariable=c1rt, background='#e6e6e6').grid(row=4, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c1he, background='#e6e6e6').grid(row=3, column=4)
Entry(scrollable_frame, textvariable=c1nrc, background='#e6e6e6').grid(row=4, column=4)
Entry(scrollable_frame, textvariable=c1ab, background='#e6e6e6').grid(row=5, column=4)


def c1entry():      # function saves entry data for case 1 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=4, column=5)
    a = c1rt.get()
    b = c1he.get()
    c = c1nrc.get()
    d = c1ab.get()

    list = ['1', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c1entry).grid(row=4, column=1)      # call save entry data function for C1

# ----- End case 1 Entry



# ----- Begin case 2 Entry

Label(scrollable_frame, text="\nCASE 2", background='white', font='Arial 12 underline').grid(row=6, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=7, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=7, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=8, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=9, column=3)

c2rt = StringVar()      # change variable type to string for user entry
c2he = StringVar()
c2nrc = StringVar()
c2ab = StringVar()
Entry(scrollable_frame, textvariable=c2rt, background='#e6e6e6').grid(row=8, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c2he, background='#e6e6e6').grid(row=7, column=4)
Entry(scrollable_frame, textvariable=c2nrc, background='#e6e6e6').grid(row=8, column=4)
Entry(scrollable_frame, textvariable=c2ab, background='#e6e6e6').grid(row=9, column=4)


def c2entry():      # function saves entry data for case 1 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=8, column=5)
    a = c2rt.get()
    b = c2he.get()
    c = c2nrc.get()
    d = c2ab.get()

    list = ['2', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c2entry).grid(row=8, column=1)      # call save entry data function for C2

# ----- End case 2 entry



# ----- Begin case 3 Entry

Label(scrollable_frame, text="\nCASE 3", background='white', font='Arial 12 underline').grid(row=10, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=11, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=11, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=12, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=13, column=3)

c3rt = StringVar()      # change variable type to string for user entry
c3he = StringVar()
c3nrc = StringVar()
c3ab = StringVar()
Entry(scrollable_frame, textvariable=c3rt, background='#e6e6e6').grid(row=12, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c3he, background='#e6e6e6').grid(row=11, column=4)
Entry(scrollable_frame, textvariable=c3nrc, background='#e6e6e6').grid(row=12, column=4)
Entry(scrollable_frame, textvariable=c3ab, background='#e6e6e6').grid(row=13, column=4)


def c3entry():      # function saves entry data for case 1 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=12, column=5)
    a = c3rt.get()
    b = c3he.get()
    c = c3nrc.get()
    d = c3ab.get()

    list = ['3', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c3entry).grid(row=12, column=1)      # call save entry data function for C2

# ----- End case 3 entry



# ----- Begin case 4 Entry

Label(scrollable_frame, text="\nCASE 4", background='white', font='Arial 12 underline').grid(row=14, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=15, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=15, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=16, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=17, column=3)

c4rt = StringVar()      # change variable type to string for user entry
c4he = StringVar()
c4nrc = StringVar()
c4ab = StringVar()
Entry(scrollable_frame, textvariable=c4rt, background='#e6e6e6').grid(row=16, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c4he, background='#e6e6e6').grid(row=15, column=4)
Entry(scrollable_frame, textvariable=c4nrc, background='#e6e6e6').grid(row=16, column=4)
Entry(scrollable_frame, textvariable=c4ab, background='#e6e6e6').grid(row=17, column=4)


def c4entry():      # function saves entry data for case 1 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=16, column=5)
    a = c4rt.get()
    b = c4he.get()
    c = c4nrc.get()
    d = c4ab.get()

    list = ['4', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c4entry).grid(row=16, column=1)      # call save entry data function for C2

# ----- End case 4 entry



# ----- Begin case 5 Entry

Label(scrollable_frame, text="\nCASE 5", background='white', font='Arial 12 underline').grid(row=18, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=19, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=19, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=20, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=21, column=3)

c5rt = StringVar()      # change variable type to string for user entry
c5he = StringVar()
c5nrc = StringVar()
c5ab = StringVar()
Entry(scrollable_frame, textvariable=c5rt, background='#e6e6e6').grid(row=20, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c5he, background='#e6e6e6').grid(row=19, column=4)
Entry(scrollable_frame, textvariable=c5nrc, background='#e6e6e6').grid(row=20, column=4)
Entry(scrollable_frame, textvariable=c5ab, background='#e6e6e6').grid(row=21, column=4)


def c5entry():      # function saves entry data for case 1 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=20, column=5)
    a = c5rt.get()
    b = c5he.get()
    c = c5nrc.get()
    d = c5ab.get()

    list = ['5', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c5entry).grid(row=20, column=1)      # call save entry data function for C2

# ----- End case 5 entry



set_wind.mainloop()

# NEXT: SAVE ENTRIES TO DATA FILE (DETERMINE HOW I WANT TO FORMAT THE FILE) REPEAT THE CODE FOR 60 ENTIRES