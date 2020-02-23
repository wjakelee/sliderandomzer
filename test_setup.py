from tkinter import *
from tkinter import messagebox
import csv


set_wind = Tk()
set_wind.title("Test Setup")                    # window title
set_wind.geometry('800x480')                    # window geometry
set_wind.configure(background='white')
frame = Frame(set_wind, background='white')
canvas = Canvas(frame, background='white')
scroll = Scrollbar(frame, orient="vertical", command=canvas.yview)      # initialize vertical scrollbar position
scrollable_frame = Frame(canvas, background='white')

canvas.configure(scrollregion=(0, 0, 800, 7600))        # window scroll length

canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
canvas.configure(yscrollcommand=scroll.set)             # set canvas to scroll

frame.place(anchor='nw', relwidth=1, relheight=1)       # Frame placement
canvas.place(anchor='nw', relwidth=1, relheight=1)      # canvas placement
scroll.pack(side='right', fill='y')                     # scroll bar placement

Label(scrollable_frame, text="TEST SETUP", background='white', font='Arial 20 bold underline').grid(row=1, column=1)
Label(scrollable_frame, text="  (SAVE every case, even empty entries)", background='white', font='Arial 12').grid(row=1, column=2, columnspan=2)

# initialize dictionaries for each case for global use
dict1 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict2 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict3 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict4 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict5 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict6 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict7 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict8 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict9 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict10 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict11 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict12 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict13 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict14 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict15 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict16 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict17 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict18 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict19 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict20 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict21 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict22 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict23 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict24 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict25 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict26 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict27 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict28 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict29 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict30 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict31 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict32 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict33 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict34 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict35 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict36 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict37 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict38 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict39 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict40 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict41 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict42 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict43 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict44 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict45 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict46 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict47 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict48 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict49 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict50 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict51 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict52 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict53 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict54 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict55 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict56 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict57 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict58 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict59 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}
dict60 = {'case': '', 'Reagent Type': '', 'h&e Slide': '', 'Nrc Slide': '', 'Ab Slide': ''}


# function creates dictionary of all user entries once all are saved
# dictionaries are then organized and written to a CSV file
def big_dictionary(list):
    global dict1, dict2, dict3, dict4, dict5, dict6, dict7, dict8, dict9, dict10, dict11, dict12, dict13, dict14, \
        dict15, dict16, dict17, dict18, dict19, dict20, dict21, dict22, dict23, dict24, dict25, dict26, dict27, \
        dict28, dict29, dict30, dict31, dict32, dict33, dict34, dict35, dict36, dict37, dict38, dict39, dict40, \
        dict41, dict42, dict43, dict44, dict45, dict46, dict47, dict48, dict49, dict50, dict51, dict52, dict53, \
        dict54, dict55, dict56, dict57, dict58, dict59, dict60

    # stores user entry in correct dictionary for each case (used to organize the CSV file)
    if list['case'] == 1:
        dict1 = list
    elif list['case'] == 2:
        dict2 = list
    elif list['case'] == 3:
        dict3 = list
    elif list['case'] == 4:
        dict4 = list
    elif list['case'] == 5:
        dict5 = list
    elif list['case'] == 6:
        dict6 = list
    elif list['case'] == 7:
        dict7 = list
    elif list['case'] == 8:
        dict8 = list
    elif list['case'] == 9:
        dict9 = list
    elif list['case'] == 10:
        dict10 = list
    elif list['case'] == 11:
        dict11 = list
    elif list['case'] == 12:
        dict12 = list
    elif list['case'] == 13:
        dict13 = list
    elif list['case'] == 14:
        dict14 = list
    elif list['case'] == 15:
        dict15 = list
    elif list['case'] == 16:
        dict16 = list
    elif list['case'] == 17:
        dict17 = list
    elif list['case'] == 18:
        dict18 = list
    elif list['case'] == 19:
        dict19 = list
    elif list['case'] == 20:
        dict20 = list
    elif list['case'] == 21:
        dict21 = list
    elif list['case'] == 22:
        dict22 = list
    elif list['case'] == 23:
        dict23 = list
    elif list['case'] == 24:
        dict24 = list
    elif list['case'] == 25:
        dict25 = list
    elif list['case'] == 26:
        dict26 = list
    elif list['case'] == 27:
        dict27 = list
    elif list['case'] == 28:
        dict28 = list
    elif list['case'] == 29:
        dict29 = list
    elif list['case'] == 30:
        dict30 = list
    elif list['case'] == 31:
        dict31 = list
    elif list['case'] == 32:
        dict32 = list
    elif list['case'] == 33:
        dict33 = list
    elif list['case'] == 34:
        dict34 = list
    elif list['case'] == 35:
        dict35 = list
    elif list['case'] == 36:
        dict36 = list
    elif list['case'] == 37:
        dict37 = list
    elif list['case'] == 38:
        dict38 = list
    elif list['case'] == 39:
        dict39 = list
    elif list['case'] == 40:
        dict40 = list
    elif list['case'] == 41:
        dict41 = list
    elif list['case'] == 42:
        dict42 = list
    elif list['case'] == 43:
        dict43 = list
    elif list['case'] == 44:
        dict44 = list
    elif list['case'] == 45:
        dict45 = list
    elif list['case'] == 46:
        dict46 = list
    elif list['case'] == 47:
        dict47 = list
    elif list['case'] == 48:
        dict48 = list
    elif list['case'] == 49:
        dict49 = list
    elif list['case'] == 50:
        dict50 = list
    elif list['case'] == 51:
        dict51 = list
    elif list['case'] == 52:
        dict52 = list
    elif list['case'] == 53:
        dict53 = list
    elif list['case'] == 54:
        dict54 = list
    elif list['case'] == 55:
        dict55 = list
    elif list['case'] == 56:
        dict56 = list
    elif list['case'] == 57:
        dict57 = list
    elif list['case'] == 58:
        dict58 = list
    elif list['case'] == 59:
        dict59 = list
    elif list['case'] == 60:
        dict60 = list

    # checks if all case entries have been saved
    if dict1['case'] == 1 and dict2['case'] == 2 and dict3['case'] == 3 and dict4['case'] == 4 and dict5['case'] == 5\
            and dict6['case'] == 6 and dict7['case'] == 7 and dict8['case'] == 8 and dict9['case'] == 9 and dict10['case'] == 10 \
            and dict11['case'] == 11 and dict12['case'] == 12 and dict13['case'] == 13 and dict14['case'] == 14 \
            and dict15['case'] == 15 and dict16['case'] == 16 and dict17['case'] == 17 and dict18['case'] == 18 \
            and dict19['case'] == 19 and dict20['case'] == 20 and dict21['case'] == 21 and dict22['case'] == 22 \
            and dict23['case'] == 23 and dict24['case'] == 24 and dict25['case'] == 25 and dict26['case'] == 26 \
            and dict27['case'] == 27 and dict28['case'] == 28 and dict29['case'] == 29 and dict30['case'] == 30 \
            and dict31['case'] == 31 and dict32['case'] == 32 and dict33['case'] == 33 and dict34['case'] == 34 \
            and dict35['case'] == 35 and dict36['case'] == 36 and dict37['case'] == 37 and dict38['case'] == 38 \
            and dict39['case'] == 39 and dict40['case'] == 40 and dict41['case'] == 41 and dict42['case'] == 42 \
            and dict43['case'] == 43 and dict44['case'] == 44 and dict45['case'] == 45 and dict46['case'] == 46 \
            and dict47['case'] == 47 and dict48['case'] == 48 and dict49['case'] == 49 and dict50['case'] == 50 \
            and dict51['case'] == 51 and dict52['case'] == 52 and dict53['case'] == 53 and dict54['case'] == 54 \
            and dict55['case'] == 55 and dict56['case'] == 56 and dict57['case'] == 57 and dict58['case'] == 58 \
            and dict59['case'] == 59 and dict60['case'] == 60:

        # organizes dictionaries into a larger dictionary
        big_dictionary = [dict1, dict2, dict3, dict4, dict5, dict6, dict7, dict8, dict9, dict10, dict11, dict12,
                          dict13, dict14, dict15, dict16, dict17, dict18, dict19, dict20, dict21, dict22, dict23,
                          dict24, dict25, dict26, dict27, dict28, dict29, dict30, dict31, dict32, dict33, dict34,
                          dict35, dict36, dict37, dict38, dict39, dict40, dict41, dict42, dict43, dict44, dict45,
                          dict46, dict47, dict48, dict49, dict50, dict51, dict52, dict53, dict54, dict55, dict56,
                          dict57, dict58, dict59, dict60]

        # writes big dictionary to CSV file when "Submit All Entries" button is pressed
        def submit_all_entries():
            with open('case_information.csv', 'w') as caseinfo_csv:
                fields = ['case', 'Reagent Type', 'h&e Slide', 'Nrc Slide', 'Ab Slide']
                csv_writer = csv.DictWriter(caseinfo_csv, fieldnames=fields)
                csv_writer.writeheader()
                for case in big_dictionary:
                    csv_writer.writerow(case)

            # notifies user that entries were saved to data file
            messagebox.showinfo("Entries Saved", "All entries saved to data file.")

        # button does not appear until all entries saved
        Button(scrollable_frame, text="Submit All Entries", background='#33adff', font='Arial 12 bold',
               command=submit_all_entries).grid(row=244, column=1, columnspan=3)


# ----- Begin case 1 Entry

# Case entry labels
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


def c1entry():      # gets values from user entry and saves values to dictionary
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=4, column=5)
    a = c1rt.get()
    b = c1he.get()
    c = c1nrc.get()
    d = c1ab.get()

    list = {'case': 1, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}    # creates dictionary
    big_dictionary(list)            # call big dictionary function


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c1entry).grid(row=4, column=1)

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

    list = {'case': 2, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c2entry).grid(row=8, column=1)

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

    list = {'case': 3, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c3entry).grid(row=12, column=1)

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

    list = {'case': 4, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c4entry).grid(row=16, column=1)

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

    list = {'case': 5, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c5entry).grid(row=20, column=1)

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

    list = {'case': 6, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c6entry).grid(row=24, column=1)

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

    list = {'case': 7, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c7entry).grid(row=28, column=1)

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

    list = {'case': 8, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c8entry).grid(row=32, column=1)

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

    list = {'case': 9, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c9entry).grid(row=36, column=1)

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

    list = {'case': 10, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c10entry).grid(row=40, column=1)      # call save entry data function

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

    list = {'case': 11, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c11entry).grid(row=44, column=1)

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

    list = {'case': 12, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c12entry).grid(row=48, column=1)

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

    list = {'case': 13, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c13entry).grid(row=52, column=1)

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

    list = {'case': 14, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c14entry).grid(row=56, column=1)

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

    list = {'case': 15, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c15entry).grid(row=60, column=1)

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

    list = {'case': 16, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c16entry).grid(row=64, column=1)

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

    list = {'case': 17, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c17entry).grid(row=68, column=1)

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

    list = {'case': 18, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c18entry).grid(row=72, column=1)

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

    list = {'case': 19, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c19entry).grid(row=76, column=1)

# ----- End case 19 entry


# ----- Begin case 20 Entry

Label(scrollable_frame, text="\nCASE 20", background='white', font='Arial 12 underline').grid(row=78, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=79, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=79, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=80, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=81, column=3)

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

    list = {'case': 20, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c20entry).grid(row=80, column=1)

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

    list = {'case': 21, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c21entry).grid(row=84, column=1)

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

    list = {'case': 22, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c22entry).grid(row=88, column=1)

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

    list = {'case': 23, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c23entry).grid(row=92, column=1)

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

    list = {'case': 24, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c24entry).grid(row=96, column=1)

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

    list = {'case': 25, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c25entry).grid(row=100, column=1)

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

    list = {'case': 26, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c26entry).grid(row=104, column=1)

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

    list = {'case': 27, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c27entry).grid(row=108, column=1)

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

    list = {'case': 28, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c28entry).grid(row=112, column=1)

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

    list = {'case': 29, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c29entry).grid(row=116, column=1)

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


def c30entry():      # function saves entry data for case 30 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=120, column=5)
    a = c30rt.get()
    b = c30he.get()
    c = c30nrc.get()
    d = c30ab.get()

    list = {'case': 30, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c30entry).grid(row=120, column=1)

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


def c31entry():      # function saves entry data for case 31 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=124, column=5)
    a = c31rt.get()
    b = c31he.get()
    c = c31nrc.get()
    d = c31ab.get()

    list = {'case': 31, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c31entry).grid(row=124, column=1)

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


def c32entry():      # function saves entry data for case 32 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=128, column=5)
    a = c32rt.get()
    b = c32he.get()
    c = c32nrc.get()
    d = c32ab.get()

    list = {'case': 32, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c32entry).grid(row=128, column=1)

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


def c33entry():      # function saves entry data for case 33 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=132, column=5)
    a = c33rt.get()
    b = c33he.get()
    c = c33nrc.get()
    d = c33ab.get()

    list = {'case': 33, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c33entry).grid(row=132, column=1)

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


def c34entry():      # function saves entry data for case 34 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=136, column=5)
    a = c34rt.get()
    b = c34he.get()
    c = c34nrc.get()
    d = c34ab.get()

    list = {'case': 34, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c34entry).grid(row=136, column=1)

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


def c35entry():      # function saves entry data for case 35 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=140, column=5)
    a = c35rt.get()
    b = c35he.get()
    c = c35nrc.get()
    d = c35ab.get()

    list = {'case': 35, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c35entry).grid(row=140, column=1)

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


def c36entry():      # function saves entry data for case 36 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=144, column=5)
    a = c36rt.get()
    b = c36he.get()
    c = c36nrc.get()
    d = c36ab.get()

    list = {'case': 36, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c36entry).grid(row=144, column=1)

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


def c37entry():      # function saves entry data for case 37 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=148, column=5)
    a = c37rt.get()
    b = c37he.get()
    c = c37nrc.get()
    d = c37ab.get()

    list = {'case': 37, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c37entry).grid(row=148, column=1)

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


def c38entry():      # function saves entry data for case 38 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=152, column=5)
    a = c38rt.get()
    b = c38he.get()
    c = c38nrc.get()
    d = c38ab.get()

    list = {'case': 38, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c38entry).grid(row=152, column=1)

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


def c39entry():      # function saves entry data for case 39 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=156, column=5)
    a = c39rt.get()
    b = c39he.get()
    c = c39nrc.get()
    d = c39ab.get()

    list = {'case': 39, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c39entry).grid(row=156, column=1)

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


def c40entry():      # function saves entry data for case 40 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=160, column=5)
    a = c40rt.get()
    b = c40he.get()
    c = c40nrc.get()
    d = c40ab.get()

    list = {'case': 40, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c40entry).grid(row=160, column=1)

# ----- End case 40 entry


# ----- Begin case 41 Entry

Label(scrollable_frame, text="\nCASE 41", background='white', font='Arial 12 underline').grid(row=162, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=163, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=163, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=164, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=165, column=3)

c41rt = StringVar()      # change variable type to string for user entry
c41he = StringVar()
c41nrc = StringVar()
c41ab = StringVar()
Entry(scrollable_frame, textvariable=c41rt, background='#e6e6e6').grid(row=164, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c41he, background='#e6e6e6').grid(row=163, column=4)
Entry(scrollable_frame, textvariable=c41nrc, background='#e6e6e6').grid(row=164, column=4)
Entry(scrollable_frame, textvariable=c41ab, background='#e6e6e6').grid(row=165, column=4)


def c41entry():      # function saves entry data for case 41 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=164, column=5)
    a = c41rt.get()
    b = c41he.get()
    c = c41nrc.get()
    d = c41ab.get()

    list = {'case': 41, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c41entry).grid(row=164, column=1)

# ----- End case 41 entry


# ----- Begin case 42 Entry

Label(scrollable_frame, text="\nCASE 41", background='white', font='Arial 12 underline').grid(row=166, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=167, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=167, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=168, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=169, column=3)

c42rt = StringVar()      # change variable type to string for user entry
c42he = StringVar()
c42nrc = StringVar()
c42ab = StringVar()
Entry(scrollable_frame, textvariable=c42rt, background='#e6e6e6').grid(row=168, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c42he, background='#e6e6e6').grid(row=167, column=4)
Entry(scrollable_frame, textvariable=c42nrc, background='#e6e6e6').grid(row=168, column=4)
Entry(scrollable_frame, textvariable=c42ab, background='#e6e6e6').grid(row=169, column=4)


def c42entry():      # function saves entry data for case 42 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=168, column=5)
    a = c42rt.get()
    b = c42he.get()
    c = c42nrc.get()
    d = c42ab.get()

    list = {'case': 42, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c42entry).grid(row=168, column=1)

# ----- End case 42 entry


# ----- Begin case 43 Entry

Label(scrollable_frame, text="\nCASE 43", background='white', font='Arial 12 underline').grid(row=170, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=171, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=171, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=172, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=173, column=3)

c43rt = StringVar()      # change variable type to string for user entry
c43he = StringVar()
c43nrc = StringVar()
c43ab = StringVar()
Entry(scrollable_frame, textvariable=c43rt, background='#e6e6e6').grid(row=172, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c43he, background='#e6e6e6').grid(row=171, column=4)
Entry(scrollable_frame, textvariable=c43nrc, background='#e6e6e6').grid(row=172, column=4)
Entry(scrollable_frame, textvariable=c43ab, background='#e6e6e6').grid(row=173, column=4)


def c43entry():      # function saves entry data for case 43 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=172, column=5)
    a = c43rt.get()
    b = c43he.get()
    c = c43nrc.get()
    d = c43ab.get()

    list = {'case': 43, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c43entry).grid(row=172, column=1)

# ----- End case 43 entry


# ----- Begin case 44 Entry

Label(scrollable_frame, text="\nCASE 44", background='white', font='Arial 12 underline').grid(row=174, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=175, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=175, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=176, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=177, column=3)

c44rt = StringVar()      # change variable type to string for user entry
c44he = StringVar()
c44nrc = StringVar()
c44ab = StringVar()
Entry(scrollable_frame, textvariable=c44rt, background='#e6e6e6').grid(row=176, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c44he, background='#e6e6e6').grid(row=175, column=4)
Entry(scrollable_frame, textvariable=c44nrc, background='#e6e6e6').grid(row=176, column=4)
Entry(scrollable_frame, textvariable=c44ab, background='#e6e6e6').grid(row=177, column=4)


def c44entry():      # function saves entry data for case 44 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=176, column=5)
    a = c44rt.get()
    b = c44he.get()
    c = c44nrc.get()
    d = c44ab.get()

    list = {'case': 44, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c44entry).grid(row=176, column=1)

# ----- End case 44 entry


# ----- Begin case 45 Entry

Label(scrollable_frame, text="\nCASE 45", background='white', font='Arial 12 underline').grid(row=178, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=179, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=179, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=180, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=181, column=3)

c45rt = StringVar()      # change variable type to string for user entry
c45he = StringVar()
c45nrc = StringVar()
c45ab = StringVar()
Entry(scrollable_frame, textvariable=c45rt, background='#e6e6e6').grid(row=180, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c45he, background='#e6e6e6').grid(row=179, column=4)
Entry(scrollable_frame, textvariable=c45nrc, background='#e6e6e6').grid(row=180, column=4)
Entry(scrollable_frame, textvariable=c45ab, background='#e6e6e6').grid(row=181, column=4)


def c45entry():      # function saves entry data for case 45 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=180, column=5)
    a = c45rt.get()
    b = c45he.get()
    c = c45nrc.get()
    d = c45ab.get()

    list = {'case': 45, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c45entry).grid(row=180, column=1)

# ----- End case 45 entry


# ----- Begin case 46 Entry

Label(scrollable_frame, text="\nCASE 46", background='white', font='Arial 12 underline').grid(row=182, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=183, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=183, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=184, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=185, column=3)

c46rt = StringVar()      # change variable type to string for user entry
c46he = StringVar()
c46nrc = StringVar()
c46ab = StringVar()
Entry(scrollable_frame, textvariable=c46rt, background='#e6e6e6').grid(row=184, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c46he, background='#e6e6e6').grid(row=183, column=4)
Entry(scrollable_frame, textvariable=c46nrc, background='#e6e6e6').grid(row=184, column=4)
Entry(scrollable_frame, textvariable=c46ab, background='#e6e6e6').grid(row=185, column=4)


def c46entry():      # function saves entry data for case 46 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=184, column=5)
    a = c46rt.get()
    b = c46he.get()
    c = c46nrc.get()
    d = c46ab.get()

    list = {'case': 46, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c46entry).grid(row=184, column=1)

# ----- End case 46 entry


# ----- Begin case 47 Entry

Label(scrollable_frame, text="\nCASE 47", background='white', font='Arial 12 underline').grid(row=186, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=187, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=187, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=188, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=189, column=3)

c47rt = StringVar()      # change variable type to string for user entry
c47he = StringVar()
c47nrc = StringVar()
c47ab = StringVar()
Entry(scrollable_frame, textvariable=c47rt, background='#e6e6e6').grid(row=188, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c47he, background='#e6e6e6').grid(row=187, column=4)
Entry(scrollable_frame, textvariable=c47nrc, background='#e6e6e6').grid(row=188, column=4)
Entry(scrollable_frame, textvariable=c47ab, background='#e6e6e6').grid(row=189, column=4)


def c47entry():      # function saves entry data for case 47 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=188, column=5)
    a = c47rt.get()
    b = c47he.get()
    c = c47nrc.get()
    d = c47ab.get()

    list = {'case': 47, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c47entry).grid(row=188, column=1)

# ----- End case 47 entry


# ----- Begin case 48 Entry

Label(scrollable_frame, text="\nCASE 48", background='white', font='Arial 12 underline').grid(row=190, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=191, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=191, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=192, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=193, column=3)

c48rt = StringVar()      # change variable type to string for user entry
c48he = StringVar()
c48nrc = StringVar()
c48ab = StringVar()
Entry(scrollable_frame, textvariable=c48rt, background='#e6e6e6').grid(row=192, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c48he, background='#e6e6e6').grid(row=191, column=4)
Entry(scrollable_frame, textvariable=c48nrc, background='#e6e6e6').grid(row=192, column=4)
Entry(scrollable_frame, textvariable=c48ab, background='#e6e6e6').grid(row=193, column=4)


def c48entry():      # function saves entry data for case 48 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=192, column=5)
    a = c48rt.get()
    b = c48he.get()
    c = c48nrc.get()
    d = c48ab.get()

    list = {'case': 48, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c48entry).grid(row=192, column=1)

# ----- End case 48 entry


# ----- Begin case 49 Entry

Label(scrollable_frame, text="\nCASE 49", background='white', font='Arial 12 underline').grid(row=194, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=195, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=195, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=196, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=197, column=3)

c49rt = StringVar()      # change variable type to string for user entry
c49he = StringVar()
c49nrc = StringVar()
c49ab = StringVar()
Entry(scrollable_frame, textvariable=c49rt, background='#e6e6e6').grid(row=196, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c49he, background='#e6e6e6').grid(row=195, column=4)
Entry(scrollable_frame, textvariable=c49nrc, background='#e6e6e6').grid(row=196, column=4)
Entry(scrollable_frame, textvariable=c49ab, background='#e6e6e6').grid(row=197, column=4)


def c49entry():      # function saves entry data for case 49 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=196, column=5)
    a = c49rt.get()
    b = c49he.get()
    c = c49nrc.get()
    d = c49ab.get()

    list = {'case': 49, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c49entry).grid(row=196, column=1)

# ----- End case 49 entry


# ----- Begin case 50 Entry

Label(scrollable_frame, text="\nCASE 50", background='white', font='Arial 12 underline').grid(row=198, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=199, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=199, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=200, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=201, column=3)

c50rt = StringVar()      # change variable type to string for user entry
c50he = StringVar()
c50nrc = StringVar()
c50ab = StringVar()
Entry(scrollable_frame, textvariable=c50rt, background='#e6e6e6').grid(row=200, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c50he, background='#e6e6e6').grid(row=199, column=4)
Entry(scrollable_frame, textvariable=c50nrc, background='#e6e6e6').grid(row=200, column=4)
Entry(scrollable_frame, textvariable=c50ab, background='#e6e6e6').grid(row=201, column=4)


def c50entry():      # function saves entry data for case 50 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=200, column=5)
    a = c50rt.get()
    b = c50he.get()
    c = c50nrc.get()
    d = c50ab.get()

    list = {'case': 50, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c50entry).grid(row=200, column=1)

# ----- End case 50 entry


# ----- Begin case 51 Entry

Label(scrollable_frame, text="\nCASE 51", background='white', font='Arial 12 underline').grid(row=202, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=203, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=203, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=204, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=205, column=3)

c51rt = StringVar()      # change variable type to string for user entry
c51he = StringVar()
c51nrc = StringVar()
c51ab = StringVar()
Entry(scrollable_frame, textvariable=c51rt, background='#e6e6e6').grid(row=204, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c51he, background='#e6e6e6').grid(row=203, column=4)
Entry(scrollable_frame, textvariable=c51nrc, background='#e6e6e6').grid(row=204, column=4)
Entry(scrollable_frame, textvariable=c51ab, background='#e6e6e6').grid(row=205, column=4)


def c51entry():      # function saves entry data for case 51 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=204, column=5)
    a = c51rt.get()
    b = c51he.get()
    c = c51nrc.get()
    d = c51ab.get()

    list = {'case': 51, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c51entry).grid(row=204, column=1)

# ----- End case 51 entry


# ----- Begin case 52 Entry

Label(scrollable_frame, text="\nCASE 52", background='white', font='Arial 12 underline').grid(row=206, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=207, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=207, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=208, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=209, column=3)

c52rt = StringVar()      # change variable type to string for user entry
c52he = StringVar()
c52nrc = StringVar()
c52ab = StringVar()
Entry(scrollable_frame, textvariable=c52rt, background='#e6e6e6').grid(row=208, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c52he, background='#e6e6e6').grid(row=207, column=4)
Entry(scrollable_frame, textvariable=c52nrc, background='#e6e6e6').grid(row=208, column=4)
Entry(scrollable_frame, textvariable=c52ab, background='#e6e6e6').grid(row=209, column=4)


def c52entry():      # function saves entry data for case 52 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=208, column=5)
    a = c52rt.get()
    b = c52he.get()
    c = c52nrc.get()
    d = c52ab.get()

    list = {'case': 52, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c52entry).grid(row=208, column=1)

# ----- End case 52 entry


# ----- Begin case 53 Entry

Label(scrollable_frame, text="\nCASE 53", background='white', font='Arial 12 underline').grid(row=210, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=211, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=211, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=212, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=213, column=3)

c53rt = StringVar()      # change variable type to string for user entry
c53he = StringVar()
c53nrc = StringVar()
c53ab = StringVar()
Entry(scrollable_frame, textvariable=c53rt, background='#e6e6e6').grid(row=212, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c53he, background='#e6e6e6').grid(row=211, column=4)
Entry(scrollable_frame, textvariable=c53nrc, background='#e6e6e6').grid(row=212, column=4)
Entry(scrollable_frame, textvariable=c53ab, background='#e6e6e6').grid(row=213, column=4)


def c53entry():      # function saves entry data for case 53 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=212, column=5)
    a = c53rt.get()
    b = c53he.get()
    c = c53nrc.get()
    d = c53ab.get()

    list = {'case': 53, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c53entry).grid(row=212, column=1)

# ----- End case 53 entry


# ----- Begin case 54 Entry

Label(scrollable_frame, text="\nCASE 54", background='white', font='Arial 12 underline').grid(row=214, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=215, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=215, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=216, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=217, column=3)

c54rt = StringVar()      # change variable type to string for user entry
c54he = StringVar()
c54nrc = StringVar()
c54ab = StringVar()
Entry(scrollable_frame, textvariable=c54rt, background='#e6e6e6').grid(row=216, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c54he, background='#e6e6e6').grid(row=215, column=4)
Entry(scrollable_frame, textvariable=c54nrc, background='#e6e6e6').grid(row=216, column=4)
Entry(scrollable_frame, textvariable=c54ab, background='#e6e6e6').grid(row=217, column=4)


def c54entry():      # function saves entry data for case 54 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=216, column=5)
    a = c54rt.get()
    b = c54he.get()
    c = c54nrc.get()
    d = c54ab.get()

    list = {'case': 54, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c54entry).grid(row=216, column=1)

# ----- End case 54 entry


# ----- Begin case 55 Entry

Label(scrollable_frame, text="\nCASE 55", background='white', font='Arial 12 underline').grid(row=218, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=219, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=219, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=220, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=221, column=3)

c55rt = StringVar()      # change variable type to string for user entry
c55he = StringVar()
c55nrc = StringVar()
c55ab = StringVar()
Entry(scrollable_frame, textvariable=c55rt, background='#e6e6e6').grid(row=220, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c55he, background='#e6e6e6').grid(row=219, column=4)
Entry(scrollable_frame, textvariable=c55nrc, background='#e6e6e6').grid(row=220, column=4)
Entry(scrollable_frame, textvariable=c55ab, background='#e6e6e6').grid(row=221, column=4)


def c55entry():      # function saves entry data for case 55 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=220, column=5)
    a = c55rt.get()
    b = c55he.get()
    c = c55nrc.get()
    d = c55ab.get()

    list = {'case': 55, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c55entry).grid(row=220, column=1)

# ----- End case 55 entry


# ----- Begin case 56 Entry

Label(scrollable_frame, text="\nCASE 56", background='white', font='Arial 12 underline').grid(row=222, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=223, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=223, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=224, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=225, column=3)

c56rt = StringVar()      # change variable type to string for user entry
c56he = StringVar()
c56nrc = StringVar()
c56ab = StringVar()
Entry(scrollable_frame, textvariable=c56rt, background='#e6e6e6').grid(row=224, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c56he, background='#e6e6e6').grid(row=223, column=4)
Entry(scrollable_frame, textvariable=c56nrc, background='#e6e6e6').grid(row=224, column=4)
Entry(scrollable_frame, textvariable=c56ab, background='#e6e6e6').grid(row=225, column=4)


def c56entry():      # function saves entry data for case 56 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=224, column=5)
    a = c56rt.get()
    b = c56he.get()
    c = c56nrc.get()
    d = c56ab.get()

    list = {'case': 56, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c56entry).grid(row=224, column=1)

# ----- End case 56 entry


# ----- Begin case 57 Entry

Label(scrollable_frame, text="\nCASE 57", background='white', font='Arial 12 underline').grid(row=226, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=227, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=227, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=228, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=229, column=3)

c57rt = StringVar()      # change variable type to string for user entry
c57he = StringVar()
c57nrc = StringVar()
c57ab = StringVar()
Entry(scrollable_frame, textvariable=c57rt, background='#e6e6e6').grid(row=228, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c57he, background='#e6e6e6').grid(row=227, column=4)
Entry(scrollable_frame, textvariable=c57nrc, background='#e6e6e6').grid(row=228, column=4)
Entry(scrollable_frame, textvariable=c57ab, background='#e6e6e6').grid(row=229, column=4)


def c57entry():      # function saves entry data for case 57 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=228, column=5)
    a = c57rt.get()
    b = c57he.get()
    c = c57nrc.get()
    d = c57ab.get()

    list = {'case': 57, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c57entry).grid(row=228, column=1)

# ----- End case 57 entry


# ----- Begin case 58 Entry

Label(scrollable_frame, text="\nCASE 58", background='white', font='Arial 12 underline').grid(row=230, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=231, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=231, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=232, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=233, column=3)

c58rt = StringVar()      # change variable type to string for user entry
c58he = StringVar()
c58nrc = StringVar()
c58ab = StringVar()
Entry(scrollable_frame, textvariable=c58rt, background='#e6e6e6').grid(row=232, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c58he, background='#e6e6e6').grid(row=231, column=4)
Entry(scrollable_frame, textvariable=c58nrc, background='#e6e6e6').grid(row=232, column=4)
Entry(scrollable_frame, textvariable=c58ab, background='#e6e6e6').grid(row=233, column=4)


def c58entry():      # function saves entry data for case 58 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=232, column=5)
    a = c58rt.get()
    b = c58he.get()
    c = c58nrc.get()
    d = c58ab.get()

    list = {'case': 58, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c58entry).grid(row=232, column=1)

# ----- End case 58 entry


# ----- Begin case 59 Entry

Label(scrollable_frame, text="\nCASE 59", background='white', font='Arial 12 underline').grid(row=234, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=235, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=235, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=236, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=237, column=3)

c59rt = StringVar()      # change variable type to string for user entry
c59he = StringVar()
c59nrc = StringVar()
c59ab = StringVar()
Entry(scrollable_frame, textvariable=c59rt, background='#e6e6e6').grid(row=236, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c59he, background='#e6e6e6').grid(row=235, column=4)
Entry(scrollable_frame, textvariable=c59nrc, background='#e6e6e6').grid(row=236, column=4)
Entry(scrollable_frame, textvariable=c59ab, background='#e6e6e6').grid(row=237, column=4)


def c59entry():      # function saves entry data for case 59 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=236, column=5)
    a = c59rt.get()
    b = c59he.get()
    c = c59nrc.get()
    d = c59ab.get()

    list = {'case': 59, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c59entry).grid(row=236, column=1)

# ----- End case 59 entry


# ----- Begin case 60 Entry

Label(scrollable_frame, text="\nCASE 60", background='white', font='Arial 12 underline').grid(row=238, column=1)
Label(scrollable_frame, text="Reagent Type:", background='white', font='Arial 12').grid(row=239, column=2)
Label(scrollable_frame, text="       h&e:", background='white', font='Arial 12').grid(row=239, column=3)
Label(scrollable_frame, text="       Nrc:", background='white', font='Arial 12').grid(row=240, column=3)
Label(scrollable_frame, text="       Ab:", background='white', font='Arial 12').grid(row=241, column=3)

c60rt = StringVar()      # change variable type to string for user entry
c60he = StringVar()
c60nrc = StringVar()
c60ab = StringVar()
Entry(scrollable_frame, textvariable=c60rt, background='#e6e6e6').grid(row=240, column=2)      # user entry bars
Entry(scrollable_frame, textvariable=c60he, background='#e6e6e6').grid(row=239, column=4)
Entry(scrollable_frame, textvariable=c60nrc, background='#e6e6e6').grid(row=240, column=4)
Entry(scrollable_frame, textvariable=c60ab, background='#e6e6e6').grid(row=241, column=4)


def c60entry():      # function saves entry data for case 60 to CSV file
    Label(scrollable_frame, text="SAVED", background='white', font='Arial 12').grid(row=240, column=5)
    a = c60rt.get()
    b = c60he.get()
    c = c60nrc.get()
    d = c60ab.get()

    list = {'case': 60, 'Reagent Type': a, 'h&e Slide': b, 'Nrc Slide': c, 'Ab Slide': d}
    big_dictionary(list)


# save entry button
Button(scrollable_frame, text="Save", background='#2eb82e', font='Arial 12 bold', command=c60entry).grid(row=240, column=1)

# ----- End case 60 entry


Label(scrollable_frame, text="\nSubmit button will not appear until all entries are saved.\n(including empty cases)",
      background='white', font='Arial 12 bold').grid(row=242, column=1, columnspan=3)


set_wind.mainloop()