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


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c1entry).grid(row=4, column=1)      # call save entry data function

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


def c2entry():      # function saves entry data for case 2 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=8, column=5)
    a = c2rt.get()
    b = c2he.get()
    c = c2nrc.get()
    d = c2ab.get()

    list = ['2', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c2entry).grid(row=8, column=1)      # call save entry data function

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


def c3entry():      # function saves entry data for case 3 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=12, column=5)
    a = c3rt.get()
    b = c3he.get()
    c = c3nrc.get()
    d = c3ab.get()

    list = ['3', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c3entry).grid(row=12, column=1)      # call save entry data function

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


def c4entry():      # function saves entry data for case 4 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=16, column=5)
    a = c4rt.get()
    b = c4he.get()
    c = c4nrc.get()
    d = c4ab.get()

    list = ['4', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c4entry).grid(row=16, column=1)      # call save entry data function

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


def c5entry():      # function saves entry data for case 5 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=20, column=5)
    a = c5rt.get()
    b = c5he.get()
    c = c5nrc.get()
    d = c5ab.get()

    list = ['5', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c5entry).grid(row=20, column=1)      # call save entry data function

# ----- End case 5 entry


# ----- Begin case 6 Entry

Label(scrollable_frame, text="\nCASE 6", background='white', font='Arial 12 underline').grid(row=22, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=23, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=23, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=24, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=25, column=3)

c6rt = StringVar()      # change variable type to string for user entry
c6he = StringVar()
c6nrc = StringVar()
c6ab = StringVar()
Entry(scrollable_frame, textvariable=c6rt, background='#e6e6e6').grid(row=24, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c6he, background='#e6e6e6').grid(row=23, column=4)
Entry(scrollable_frame, textvariable=c6nrc, background='#e6e6e6').grid(row=24, column=4)
Entry(scrollable_frame, textvariable=c6ab, background='#e6e6e6').grid(row=25, column=4)


def c6entry():      # function saves entry data for case 6 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=24, column=5)
    a = c6rt.get()
    b = c6he.get()
    c = c6nrc.get()
    d = c6ab.get()

    list = ['6', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c6entry).grid(row=24, column=1)      # call save entry data function

# ----- End case 6 entry


# ----- Begin case 7 Entry

Label(scrollable_frame, text="\nCASE 7", background='white', font='Arial 12 underline').grid(row=26, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=27, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=27, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=28, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=29, column=3)

c7rt = StringVar()      # change variable type to string for user entry
c7he = StringVar()
c7nrc = StringVar()
c7ab = StringVar()
Entry(scrollable_frame, textvariable=c7rt, background='#e6e6e6').grid(row=28, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c7he, background='#e6e6e6').grid(row=27, column=4)
Entry(scrollable_frame, textvariable=c7nrc, background='#e6e6e6').grid(row=28, column=4)
Entry(scrollable_frame, textvariable=c7ab, background='#e6e6e6').grid(row=29, column=4)


def c7entry():      # function saves entry data for case 7 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=28, column=5)
    a = c7rt.get()
    b = c7he.get()
    c = c7nrc.get()
    d = c7ab.get()

    list = ['7', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c7entry).grid(row=28, column=1)      # call save entry data function

# ----- End case 7 entry


# ----- Begin case 8 Entry

Label(scrollable_frame, text="\nCASE 8", background='white', font='Arial 12 underline').grid(row=30, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=31, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=31, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=32, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=33, column=3)

c8rt = StringVar()      # change variable type to string for user entry
c8he = StringVar()
c8nrc = StringVar()
c8ab = StringVar()
Entry(scrollable_frame, textvariable=c8rt, background='#e6e6e6').grid(row=32, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c8he, background='#e6e6e6').grid(row=31, column=4)
Entry(scrollable_frame, textvariable=c8nrc, background='#e6e6e6').grid(row=32, column=4)
Entry(scrollable_frame, textvariable=c8ab, background='#e6e6e6').grid(row=33, column=4)


def c8entry():      # function saves entry data for case 8 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=32, column=5)
    a = c8rt.get()
    b = c8he.get()
    c = c8nrc.get()
    d = c8ab.get()

    list = ['8', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c8entry).grid(row=32, column=1)      # call save entry data function

# ----- End case 8 entry


# ----- Begin case 9 Entry

Label(scrollable_frame, text="\nCASE 9", background='white', font='Arial 12 underline').grid(row=34, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=35, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=35, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=36, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=37, column=3)

c9rt = StringVar()      # change variable type to string for user entry
c9he = StringVar()
c9nrc = StringVar()
c9ab = StringVar()
Entry(scrollable_frame, textvariable=c9rt, background='#e6e6e6').grid(row=36, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c9he, background='#e6e6e6').grid(row=35, column=4)
Entry(scrollable_frame, textvariable=c9nrc, background='#e6e6e6').grid(row=36, column=4)
Entry(scrollable_frame, textvariable=c9ab, background='#e6e6e6').grid(row=37, column=4)


def c9entry():      # function saves entry data for case 9 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=36, column=5)
    a = c9rt.get()
    b = c9he.get()
    c = c9nrc.get()
    d = c9ab.get()

    list = ['9', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c9entry).grid(row=36, column=1)      # call save entry data function

# ----- End case 9 entry


# ----- Begin case 10 Entry

Label(scrollable_frame, text="\nCASE 10", background='white', font='Arial 12 underline').grid(row=38, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=39, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=39, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=40, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=41, column=3)

c10rt = StringVar()      # change variable type to string for user entry
c10he = StringVar()
c10nrc = StringVar()
c10ab = StringVar()
Entry(scrollable_frame, textvariable=c10rt, background='#e6e6e6').grid(row=40, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c10he, background='#e6e6e6').grid(row=39, column=4)
Entry(scrollable_frame, textvariable=c10nrc, background='#e6e6e6').grid(row=40, column=4)
Entry(scrollable_frame, textvariable=c10ab, background='#e6e6e6').grid(row=41, column=4)


def c10entry():      # function saves entry data for case 10 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=40, column=5)
    a = c10rt.get()
    b = c10he.get()
    c = c10nrc.get()
    d = c10ab.get()

    list = ['10', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c10entry).grid(row=40, column=1)      # call save entry data function

# ----- End case 10 entry


# ----- Begin case 11 Entry

Label(scrollable_frame, text="\nCASE 11", background='white', font='Arial 12 underline').grid(row=42, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=43, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=43, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=44, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=45, column=3)

c11rt = StringVar()      # change variable type to string for user entry
c11he = StringVar()
c11nrc = StringVar()
c11ab = StringVar()
Entry(scrollable_frame, textvariable=c11rt, background='#e6e6e6').grid(row=44, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c11he, background='#e6e6e6').grid(row=43, column=4)
Entry(scrollable_frame, textvariable=c11nrc, background='#e6e6e6').grid(row=44, column=4)
Entry(scrollable_frame, textvariable=c11ab, background='#e6e6e6').grid(row=45, column=4)


def c11entry():      # function saves entry data for case 11 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=44, column=5)
    a = c11rt.get()
    b = c11he.get()
    c = c11nrc.get()
    d = c11ab.get()

    list = ['11', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c11entry).grid(row=44, column=1)      # call save entry data function

# ----- End case 11 entry


# ----- Begin case 12 Entry

Label(scrollable_frame, text="\nCASE 12", background='white', font='Arial 12 underline').grid(row=46, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=47, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=47, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=48, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=49, column=3)

c12rt = StringVar()      # change variable type to string for user entry
c12he = StringVar()
c12nrc = StringVar()
c12ab = StringVar()
Entry(scrollable_frame, textvariable=c12rt, background='#e6e6e6').grid(row=48, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c12he, background='#e6e6e6').grid(row=47, column=4)
Entry(scrollable_frame, textvariable=c12nrc, background='#e6e6e6').grid(row=48, column=4)
Entry(scrollable_frame, textvariable=c12ab, background='#e6e6e6').grid(row=49, column=4)


def c12entry():      # function saves entry data for case 12 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=48, column=5)
    a = c12rt.get()
    b = c12he.get()
    c = c12nrc.get()
    d = c12ab.get()

    list = ['12', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c12entry).grid(row=48, column=1)      # call save entry data function

# ----- End case 12 entry


# ----- Begin case 13 Entry

Label(scrollable_frame, text="\nCASE 13", background='white', font='Arial 12 underline').grid(row=50, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=51, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=51, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=52, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=53, column=3)

c13rt = StringVar()      # change variable type to string for user entry
c13he = StringVar()
c13nrc = StringVar()
c13ab = StringVar()
Entry(scrollable_frame, textvariable=c13rt, background='#e6e6e6').grid(row=52, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c13he, background='#e6e6e6').grid(row=51, column=4)
Entry(scrollable_frame, textvariable=c13nrc, background='#e6e6e6').grid(row=52, column=4)
Entry(scrollable_frame, textvariable=c13ab, background='#e6e6e6').grid(row=53, column=4)


def c13entry():      # function saves entry data for case 13 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=52, column=5)
    a = c13rt.get()
    b = c13he.get()
    c = c13nrc.get()
    d = c13ab.get()

    list = ['13', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c13entry).grid(row=52, column=1)      # call save entry data function

# ----- End case 13 entry


# ----- Begin case 14 Entry

Label(scrollable_frame, text="\nCASE 14", background='white', font='Arial 12 underline').grid(row=54, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=55, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=55, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=56, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=57, column=3)

c14rt = StringVar()      # change variable type to string for user entry
c14he = StringVar()
c14nrc = StringVar()
c14ab = StringVar()
Entry(scrollable_frame, textvariable=c14rt, background='#e6e6e6').grid(row=56, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c14he, background='#e6e6e6').grid(row=55, column=4)
Entry(scrollable_frame, textvariable=c14nrc, background='#e6e6e6').grid(row=56, column=4)
Entry(scrollable_frame, textvariable=c14ab, background='#e6e6e6').grid(row=57, column=4)


def c14entry():      # function saves entry data for case 14 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=56, column=5)
    a = c14rt.get()
    b = c14he.get()
    c = c14nrc.get()
    d = c14ab.get()

    list = ['14', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c14entry).grid(row=56, column=1)      # call save entry data function

# ----- End case 14 entry


# ----- Begin case 15 Entry

Label(scrollable_frame, text="\nCASE 15", background='white', font='Arial 12 underline').grid(row=58, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=59, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=59, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=60, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=61, column=3)

c15rt = StringVar()      # change variable type to string for user entry
c15he = StringVar()
c15nrc = StringVar()
c15ab = StringVar()
Entry(scrollable_frame, textvariable=c15rt, background='#e6e6e6').grid(row=60, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c15he, background='#e6e6e6').grid(row=59, column=4)
Entry(scrollable_frame, textvariable=c15nrc, background='#e6e6e6').grid(row=60, column=4)
Entry(scrollable_frame, textvariable=c15ab, background='#e6e6e6').grid(row=61, column=4)


def c15entry():      # function saves entry data for case 15 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=60, column=5)
    a = c15rt.get()
    b = c15he.get()
    c = c15nrc.get()
    d = c15ab.get()

    list = ['15', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c15entry).grid(row=60, column=1)      # call save entry data function

# ----- End case 15 entry



# ----- Begin case 16 Entry

Label(scrollable_frame, text="\nCASE 16", background='white', font='Arial 12 underline').grid(row=62, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=63, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=63, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=64, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=65, column=3)

c16rt = StringVar()      # change variable type to string for user entry
c16he = StringVar()
c16nrc = StringVar()
c16ab = StringVar()
Entry(scrollable_frame, textvariable=c16rt, background='#e6e6e6').grid(row=64, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c16he, background='#e6e6e6').grid(row=63, column=4)
Entry(scrollable_frame, textvariable=c16nrc, background='#e6e6e6').grid(row=64, column=4)
Entry(scrollable_frame, textvariable=c16ab, background='#e6e6e6').grid(row=65, column=4)


def c16entry():      # function saves entry data for case 16 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=64, column=5)
    a = c16rt.get()
    b = c16he.get()
    c = c16nrc.get()
    d = c16ab.get()

    list = ['16', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c16entry).grid(row=64, column=1)      # call save entry data function

# ----- End case 16 entry



# ----- Begin case 17 Entry

Label(scrollable_frame, text="\nCASE 17", background='white', font='Arial 12 underline').grid(row=66, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=67, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=67, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=68, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=69, column=3)

c17rt = StringVar()      # change variable type to string for user entry
c17he = StringVar()
c17nrc = StringVar()
c17ab = StringVar()
Entry(scrollable_frame, textvariable=c17rt, background='#e6e6e6').grid(row=68, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c17he, background='#e6e6e6').grid(row=67, column=4)
Entry(scrollable_frame, textvariable=c17nrc, background='#e6e6e6').grid(row=68, column=4)
Entry(scrollable_frame, textvariable=c17ab, background='#e6e6e6').grid(row=69, column=4)


def c17entry():      # function saves entry data for case 17 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=68, column=5)
    a = c17rt.get()
    b = c17he.get()
    c = c17nrc.get()
    d = c17ab.get()

    list = ['17', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c17entry).grid(row=68, column=1)      # call save entry data function

# ----- End case 17 entry


# ----- Begin case 18 Entry

Label(scrollable_frame, text="\nCASE 18", background='white', font='Arial 12 underline').grid(row=70, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=71, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=71, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=72, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=73, column=3)

c18rt = StringVar()      # change variable type to string for user entry
c18he = StringVar()
c18nrc = StringVar()
c18ab = StringVar()
Entry(scrollable_frame, textvariable=c18rt, background='#e6e6e6').grid(row=72, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c18he, background='#e6e6e6').grid(row=71, column=4)
Entry(scrollable_frame, textvariable=c18nrc, background='#e6e6e6').grid(row=72, column=4)
Entry(scrollable_frame, textvariable=c18ab, background='#e6e6e6').grid(row=73, column=4)


def c18entry():      # function saves entry data for case 18 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=72, column=5)
    a = c18rt.get()
    b = c18he.get()
    c = c18nrc.get()
    d = c18ab.get()

    list = ['18', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c18entry).grid(row=72, column=1)      # call save entry data function

# ----- End case 18 entry


# ----- Begin case 19 Entry

Label(scrollable_frame, text="\nCASE 19", background='white', font='Arial 12 underline').grid(row=74, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=75, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=75, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=76, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=77, column=3)

c19rt = StringVar()      # change variable type to string for user entry
c19he = StringVar()
c19nrc = StringVar()
c19ab = StringVar()
Entry(scrollable_frame, textvariable=c19rt, background='#e6e6e6').grid(row=76, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c19he, background='#e6e6e6').grid(row=75, column=4)
Entry(scrollable_frame, textvariable=c19nrc, background='#e6e6e6').grid(row=76, column=4)
Entry(scrollable_frame, textvariable=c19ab, background='#e6e6e6').grid(row=77, column=4)


def c19entry():      # function saves entry data for case 19 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=76, column=5)
    a = c19rt.get()
    b = c19he.get()
    c = c19nrc.get()
    d = c19ab.get()

    list = ['19', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c19entry).grid(row=76, column=1)      # call save entry data function

# ----- End case 19 entry


# ----- Begin case 20 Entry

Label(scrollable_frame, text="\nCASE 20", background='white', font='Arial 12 underline').grid(row=78, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=79, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=79, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=80, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=87, column=3)

c20rt = StringVar()      # change variable type to string for user entry
c20he = StringVar()
c20nrc = StringVar()
c20ab = StringVar()
Entry(scrollable_frame, textvariable=c20rt, background='#e6e6e6').grid(row=80, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c20he, background='#e6e6e6').grid(row=79, column=4)
Entry(scrollable_frame, textvariable=c20nrc, background='#e6e6e6').grid(row=80, column=4)
Entry(scrollable_frame, textvariable=c20ab, background='#e6e6e6').grid(row=81, column=4)


def c20entry():      # function saves entry data for case 20 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=80, column=5)
    a = c20rt.get()
    b = c20he.get()
    c = c20nrc.get()
    d = c20ab.get()

    list = ['20', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c20entry).grid(row=80, column=1)      # call save entry data function

# ----- End case 20 entry


# ----- Begin case 21 Entry

Label(scrollable_frame, text="\nCASE 21", background='white', font='Arial 12 underline').grid(row=82, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=83, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=83, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=84, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=85, column=3)

c21rt = StringVar()      # change variable type to string for user entry
c21he = StringVar()
c21nrc = StringVar()
c21ab = StringVar()
Entry(scrollable_frame, textvariable=c21rt, background='#e6e6e6').grid(row=84, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c21he, background='#e6e6e6').grid(row=83, column=4)
Entry(scrollable_frame, textvariable=c21nrc, background='#e6e6e6').grid(row=84, column=4)
Entry(scrollable_frame, textvariable=c21ab, background='#e6e6e6').grid(row=85, column=4)


def c21entry():      # function saves entry data for case 21 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=84, column=5)
    a = c21rt.get()
    b = c21he.get()
    c = c21nrc.get()
    d = c21ab.get()

    list = ['21', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c21entry).grid(row=84, column=1)      # call save entry data function

# ----- End case 21 entry


# ----- Begin case 22 Entry

Label(scrollable_frame, text="\nCASE 22", background='white', font='Arial 12 underline').grid(row=86, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=87, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=87, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=88, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=89, column=3)

c22rt = StringVar()      # change variable type to string for user entry
c22he = StringVar()
c22nrc = StringVar()
c22ab = StringVar()
Entry(scrollable_frame, textvariable=c22rt, background='#e6e6e6').grid(row=88, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c22he, background='#e6e6e6').grid(row=87, column=4)
Entry(scrollable_frame, textvariable=c22nrc, background='#e6e6e6').grid(row=88, column=4)
Entry(scrollable_frame, textvariable=c22ab, background='#e6e6e6').grid(row=89, column=4)


def c22entry():      # function saves entry data for case 22 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=88, column=5)
    a = c22rt.get()
    b = c22he.get()
    c = c22nrc.get()
    d = c22ab.get()

    list = ['22', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c22entry).grid(row=88, column=1)      # call save entry data function

# ----- End case 22 entry


# ----- Begin case 23 Entry

Label(scrollable_frame, text="\nCASE 23", background='white', font='Arial 12 underline').grid(row=90, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=91, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=91, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=92, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=93, column=3)

c23rt = StringVar()      # change variable type to string for user entry
c23he = StringVar()
c23nrc = StringVar()
c23ab = StringVar()
Entry(scrollable_frame, textvariable=c23rt, background='#e6e6e6').grid(row=92, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c23he, background='#e6e6e6').grid(row=91, column=4)
Entry(scrollable_frame, textvariable=c23nrc, background='#e6e6e6').grid(row=92, column=4)
Entry(scrollable_frame, textvariable=c23ab, background='#e6e6e6').grid(row=93, column=4)


def c23entry():      # function saves entry data for case 23 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=92, column=5)
    a = c23rt.get()
    b = c23he.get()
    c = c23nrc.get()
    d = c23ab.get()

    list = ['23', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c23entry).grid(row=92, column=1)      # call save entry data function

# ----- End case 23 entry


# ----- Begin case 24 Entry

Label(scrollable_frame, text="\nCASE 24", background='white', font='Arial 12 underline').grid(row=94, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=95, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=95, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=96, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=97, column=3)

c24rt = StringVar()      # change variable type to string for user entry
c24he = StringVar()
c24nrc = StringVar()
c24ab = StringVar()
Entry(scrollable_frame, textvariable=c24rt, background='#e6e6e6').grid(row=96, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c24he, background='#e6e6e6').grid(row=95, column=4)
Entry(scrollable_frame, textvariable=c24nrc, background='#e6e6e6').grid(row=96, column=4)
Entry(scrollable_frame, textvariable=c24ab, background='#e6e6e6').grid(row=97, column=4)


def c24entry():      # function saves entry data for case 24 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=96, column=5)
    a = c24rt.get()
    b = c24he.get()
    c = c24nrc.get()
    d = c24ab.get()

    list = ['24', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c24entry).grid(row=96, column=1)      # call save entry data function

# ----- End case 24 entry


# ----- Begin case 25 Entry

Label(scrollable_frame, text="\nCASE 25", background='white', font='Arial 12 underline').grid(row=98, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=99, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=99, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=100, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=101, column=3)

c25rt = StringVar()      # change variable type to string for user entry
c25he = StringVar()
c25nrc = StringVar()
c25ab = StringVar()
Entry(scrollable_frame, textvariable=c25rt, background='#e6e6e6').grid(row=100, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c25he, background='#e6e6e6').grid(row=99, column=4)
Entry(scrollable_frame, textvariable=c25nrc, background='#e6e6e6').grid(row=100, column=4)
Entry(scrollable_frame, textvariable=c25ab, background='#e6e6e6').grid(row=101, column=4)


def c25entry():      # function saves entry data for case 25 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=100, column=5)
    a = c25rt.get()
    b = c25he.get()
    c = c25nrc.get()
    d = c25ab.get()

    list = ['25', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c25entry).grid(row=100, column=1)      # call save entry data function

# ----- End case 25 entry


# ----- Begin case 26 Entry

Label(scrollable_frame, text="\nCASE 26", background='white', font='Arial 12 underline').grid(row=102, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=103, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=103, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=104, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=105, column=3)

c26rt = StringVar()      # change variable type to string for user entry
c26he = StringVar()
c26nrc = StringVar()
c26ab = StringVar()
Entry(scrollable_frame, textvariable=c26rt, background='#e6e6e6').grid(row=104, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c26he, background='#e6e6e6').grid(row=103, column=4)
Entry(scrollable_frame, textvariable=c26nrc, background='#e6e6e6').grid(row=104, column=4)
Entry(scrollable_frame, textvariable=c26ab, background='#e6e6e6').grid(row=105, column=4)


def c26entry():      # function saves entry data for case 26 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=104, column=5)
    a = c26rt.get()
    b = c26he.get()
    c = c26nrc.get()
    d = c26ab.get()

    list = ['26', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c26entry).grid(row=104, column=1)      # call save entry data function

# ----- End case 26 entry


# ----- Begin case 27 Entry

Label(scrollable_frame, text="\nCASE 27", background='white', font='Arial 12 underline').grid(row=106, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=107, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=107, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=108, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=109, column=3)

c27rt = StringVar()      # change variable type to string for user entry
c27he = StringVar()
c27nrc = StringVar()
c27ab = StringVar()
Entry(scrollable_frame, textvariable=c27rt, background='#e6e6e6').grid(row=108, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c27he, background='#e6e6e6').grid(row=107, column=4)
Entry(scrollable_frame, textvariable=c27nrc, background='#e6e6e6').grid(row=108, column=4)
Entry(scrollable_frame, textvariable=c27ab, background='#e6e6e6').grid(row=109, column=4)


def c27entry():      # function saves entry data for case 27 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=108, column=5)
    a = c27rt.get()
    b = c27he.get()
    c = c27nrc.get()
    d = c27ab.get()

    list = ['27', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c27entry).grid(row=108, column=1)      # call save entry data function

# ----- End case 27 entry


# ----- Begin case 28 Entry

Label(scrollable_frame, text="\nCASE 28", background='white', font='Arial 12 underline').grid(row=110, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=111, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=111, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=112, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=113, column=3)

c28rt = StringVar()      # change variable type to string for user entry
c28he = StringVar()
c28nrc = StringVar()
c28ab = StringVar()
Entry(scrollable_frame, textvariable=c28rt, background='#e6e6e6').grid(row=112, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c28he, background='#e6e6e6').grid(row=111, column=4)
Entry(scrollable_frame, textvariable=c28nrc, background='#e6e6e6').grid(row=112, column=4)
Entry(scrollable_frame, textvariable=c28ab, background='#e6e6e6').grid(row=113, column=4)


def c28entry():      # function saves entry data for case 28 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=112, column=5)
    a = c28rt.get()
    b = c28he.get()
    c = c28nrc.get()
    d = c28ab.get()

    list = ['28', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c28entry).grid(row=112, column=1)      # call save entry data function

# ----- End case 28 entry


# ----- Begin case 29 Entry

Label(scrollable_frame, text="\nCASE 29", background='white', font='Arial 12 underline').grid(row=114, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=115, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=115, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=116, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=117, column=3)

c29rt = StringVar()      # change variable type to string for user entry
c29he = StringVar()
c29nrc = StringVar()
c29ab = StringVar()
Entry(scrollable_frame, textvariable=c29rt, background='#e6e6e6').grid(row=116, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c29he, background='#e6e6e6').grid(row=115, column=4)
Entry(scrollable_frame, textvariable=c29nrc, background='#e6e6e6').grid(row=116, column=4)
Entry(scrollable_frame, textvariable=c29ab, background='#e6e6e6').grid(row=117, column=4)


def c29entry():      # function saves entry data for case 29 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=116, column=5)
    a = c29rt.get()
    b = c29he.get()
    c = c29nrc.get()
    d = c29ab.get()

    list = ['29', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c29entry).grid(row=116, column=1)      # call save entry data function

# ----- End case 29 entry


# ----- Begin case 30 Entry

Label(scrollable_frame, text="\nCASE 30", background='white', font='Arial 12 underline').grid(row=118, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=119, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=119, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=120, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=121, column=3)

c30rt = StringVar()      # change variable type to string for user entry
c30he = StringVar()
c30nrc = StringVar()
c30ab = StringVar()
Entry(scrollable_frame, textvariable=c30rt, background='#e6e6e6').grid(row=120, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c30he, background='#e6e6e6').grid(row=119, column=4)
Entry(scrollable_frame, textvariable=c30nrc, background='#e6e6e6').grid(row=120, column=4)
Entry(scrollable_frame, textvariable=c30ab, background='#e6e6e6').grid(row=121, column=4)


def c30entry():      # function saves entry data for case 29 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=120, column=5)
    a = c30rt.get()
    b = c30he.get()
    c = c30nrc.get()
    d = c30ab.get()

    list = ['30', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c30entry).grid(row=120, column=1)      # call save entry data function

# ----- End case 30 entry


# ----- Begin case 31 Entry

Label(scrollable_frame, text="\nCASE 31", background='white', font='Arial 12 underline').grid(row=122, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=123, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=123, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=124, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=125, column=3)

c31rt = StringVar()      # change variable type to string for user entry
c31he = StringVar()
c31nrc = StringVar()
c31ab = StringVar()
Entry(scrollable_frame, textvariable=c31rt, background='#e6e6e6').grid(row=124, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c31he, background='#e6e6e6').grid(row=123, column=4)
Entry(scrollable_frame, textvariable=c31nrc, background='#e6e6e6').grid(row=124, column=4)
Entry(scrollable_frame, textvariable=c31ab, background='#e6e6e6').grid(row=125, column=4)


def c31entry():      # function saves entry data for case 29 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=124, column=5)
    a = c31rt.get()
    b = c31he.get()
    c = c31nrc.get()
    d = c31ab.get()

    list = ['31', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c31entry).grid(row=124, column=1)      # call save entry data function

# ----- End case 31 entry


# ----- Begin case 32 Entry

Label(scrollable_frame, text="\nCASE 32", background='white', font='Arial 12 underline').grid(row=126, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=127, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=127, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=128, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=129, column=3)

c32rt = StringVar()      # change variable type to string for user entry
c32he = StringVar()
c32nrc = StringVar()
c32ab = StringVar()
Entry(scrollable_frame, textvariable=c32rt, background='#e6e6e6').grid(row=128, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c32he, background='#e6e6e6').grid(row=127, column=4)
Entry(scrollable_frame, textvariable=c32nrc, background='#e6e6e6').grid(row=128, column=4)
Entry(scrollable_frame, textvariable=c32ab, background='#e6e6e6').grid(row=129, column=4)


def c32entry():      # function saves entry data for case 29 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=128, column=5)
    a = c32rt.get()
    b = c32he.get()
    c = c32nrc.get()
    d = c32ab.get()

    list = ['32', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c32entry).grid(row=128, column=1)      # call save entry data function

# ----- End case 32 entry


# ----- Begin case 33 Entry

Label(scrollable_frame, text="\nCASE 33", background='white', font='Arial 12 underline').grid(row=130, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=131, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=131, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=132, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=133, column=3)

c33rt = StringVar()      # change variable type to string for user entry
c33he = StringVar()
c33nrc = StringVar()
c33ab = StringVar()
Entry(scrollable_frame, textvariable=c33rt, background='#e6e6e6').grid(row=132, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c33he, background='#e6e6e6').grid(row=131, column=4)
Entry(scrollable_frame, textvariable=c33nrc, background='#e6e6e6').grid(row=132, column=4)
Entry(scrollable_frame, textvariable=c33ab, background='#e6e6e6').grid(row=133, column=4)


def c33entry():      # function saves entry data for case 29 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=132, column=5)
    a = c33rt.get()
    b = c33he.get()
    c = c33nrc.get()
    d = c33ab.get()

    list = ['33', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c33entry).grid(row=132, column=1)      # call save entry data function

# ----- End case 33 entry


# ----- Begin case 34 Entry

Label(scrollable_frame, text="\nCASE 34", background='white', font='Arial 12 underline').grid(row=134, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=135, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=135, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=136, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=137, column=3)

c34rt = StringVar()      # change variable type to string for user entry
c34he = StringVar()
c34nrc = StringVar()
c34ab = StringVar()
Entry(scrollable_frame, textvariable=c34rt, background='#e6e6e6').grid(row=136, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c34he, background='#e6e6e6').grid(row=135, column=4)
Entry(scrollable_frame, textvariable=c34nrc, background='#e6e6e6').grid(row=136, column=4)
Entry(scrollable_frame, textvariable=c34ab, background='#e6e6e6').grid(row=137, column=4)


def c34entry():      # function saves entry data for case 29 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=136, column=5)
    a = c34rt.get()
    b = c34he.get()
    c = c34nrc.get()
    d = c34ab.get()

    list = ['34', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c34entry).grid(row=136, column=1)      # call save entry data function

# ----- End case 34 entry


# ----- Begin case 35 Entry

Label(scrollable_frame, text="\nCASE 35", background='white', font='Arial 12 underline').grid(row=138, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=139, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=139, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=140, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=141, column=3)

c35rt = StringVar()      # change variable type to string for user entry
c35he = StringVar()
c35nrc = StringVar()
c35ab = StringVar()
Entry(scrollable_frame, textvariable=c35rt, background='#e6e6e6').grid(row=140, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c35he, background='#e6e6e6').grid(row=139, column=4)
Entry(scrollable_frame, textvariable=c35nrc, background='#e6e6e6').grid(row=140, column=4)
Entry(scrollable_frame, textvariable=c35ab, background='#e6e6e6').grid(row=141, column=4)


def c35entry():      # function saves entry data for case 29 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=140, column=5)
    a = c35rt.get()
    b = c35he.get()
    c = c35nrc.get()
    d = c35ab.get()

    list = ['35', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c35entry).grid(row=140, column=1)      # call save entry data function

# ----- End case 35 entry


# ----- Begin case 36 Entry

Label(scrollable_frame, text="\nCASE 36", background='white', font='Arial 12 underline').grid(row=142, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=143, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=143, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=144, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=145, column=3)

c36rt = StringVar()      # change variable type to string for user entry
c36he = StringVar()
c36nrc = StringVar()
c36ab = StringVar()
Entry(scrollable_frame, textvariable=c36rt, background='#e6e6e6').grid(row=144, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c36he, background='#e6e6e6').grid(row=143, column=4)
Entry(scrollable_frame, textvariable=c36nrc, background='#e6e6e6').grid(row=144, column=4)
Entry(scrollable_frame, textvariable=c36ab, background='#e6e6e6').grid(row=145, column=4)


def c36entry():      # function saves entry data for case 29 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=144, column=5)
    a = c36rt.get()
    b = c36he.get()
    c = c36nrc.get()
    d = c36ab.get()

    list = ['36', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c36entry).grid(row=144, column=1)      # call save entry data function

# ----- End case 36 entry


# ----- Begin case 37 Entry

Label(scrollable_frame, text="\nCASE 37", background='white', font='Arial 12 underline').grid(row=146, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=147, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=147, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=148, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=149, column=3)

c37rt = StringVar()      # change variable type to string for user entry
c37he = StringVar()
c37nrc = StringVar()
c37ab = StringVar()
Entry(scrollable_frame, textvariable=c37rt, background='#e6e6e6').grid(row=148, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c37he, background='#e6e6e6').grid(row=147, column=4)
Entry(scrollable_frame, textvariable=c37nrc, background='#e6e6e6').grid(row=148, column=4)
Entry(scrollable_frame, textvariable=c37ab, background='#e6e6e6').grid(row=149, column=4)


def c37entry():      # function saves entry data for case 29 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=148, column=5)
    a = c37rt.get()
    b = c37he.get()
    c = c37nrc.get()
    d = c37ab.get()

    list = ['37', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c37entry).grid(row=148, column=1)      # call save entry data function

# ----- End case 37 entry


# ----- Begin case 38 Entry

Label(scrollable_frame, text="\nCASE 38", background='white', font='Arial 12 underline').grid(row=150, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=151, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=151, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=152, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=153, column=3)

c38rt = StringVar()      # change variable type to string for user entry
c38he = StringVar()
c38nrc = StringVar()
c38ab = StringVar()
Entry(scrollable_frame, textvariable=c38rt, background='#e6e6e6').grid(row=152, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c38he, background='#e6e6e6').grid(row=151, column=4)
Entry(scrollable_frame, textvariable=c38nrc, background='#e6e6e6').grid(row=152, column=4)
Entry(scrollable_frame, textvariable=c38ab, background='#e6e6e6').grid(row=153, column=4)


def c38entry():      # function saves entry data for case 29 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=152, column=5)
    a = c38rt.get()
    b = c38he.get()
    c = c38nrc.get()
    d = c38ab.get()

    list = ['38', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c38entry).grid(row=152, column=1)      # call save entry data function

# ----- End case 38 entry


# ----- Begin case 39 Entry

Label(scrollable_frame, text="\nCASE 39", background='white', font='Arial 12 underline').grid(row=154, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=155, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=155, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=156, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=157, column=3)

c39rt = StringVar()      # change variable type to string for user entry
c39he = StringVar()
c39nrc = StringVar()
c39ab = StringVar()
Entry(scrollable_frame, textvariable=c39rt, background='#e6e6e6').grid(row=156, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c39he, background='#e6e6e6').grid(row=155, column=4)
Entry(scrollable_frame, textvariable=c39nrc, background='#e6e6e6').grid(row=156, column=4)
Entry(scrollable_frame, textvariable=c39ab, background='#e6e6e6').grid(row=157, column=4)


def c39entry():      # function saves entry data for case 29 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=156, column=5)
    a = c39rt.get()
    b = c39he.get()
    c = c39nrc.get()
    d = c39ab.get()

    list = ['39', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c39entry).grid(row=156, column=1)      # call save entry data function

# ----- End case 39 entry


# ----- Begin case 40 Entry

Label(scrollable_frame, text="\nCASE 40", background='white', font='Arial 12 underline').grid(row=158, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=159, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=159, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=160, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=161, column=3)

c40rt = StringVar()      # change variable type to string for user entry
c40he = StringVar()
c40nrc = StringVar()
c40ab = StringVar()
Entry(scrollable_frame, textvariable=c40rt, background='#e6e6e6').grid(row=160, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c40he, background='#e6e6e6').grid(row=159, column=4)
Entry(scrollable_frame, textvariable=c40nrc, background='#e6e6e6').grid(row=160, column=4)
Entry(scrollable_frame, textvariable=c40ab, background='#e6e6e6').grid(row=161, column=4)


def c40entry():      # function saves entry data for case 29 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=160, column=5)
    a = c40rt.get()
    b = c40he.get()
    c = c40nrc.get()
    d = c40ab.get()

    list = ['40', a, b, c, d]
    with open('case_information.csv', 'a') as caseinfo_csv:
        csv_writer = csv.writer(caseinfo_csv)
        csv_writer.writerow(list)


Button(scrollable_frame, text="Save", background='green', font='Arial 12 bold', command=c40entry).grid(row=160, column=1)      # call save entry data function

# ----- End case 40 entry



set_wind.mainloop()

# NEXT: SAVE ENTRIES TO DATA FILE (DETERMINE HOW I WANT TO FORMAT THE FILE) REPEAT THE CODE FOR 60 ENTIRES