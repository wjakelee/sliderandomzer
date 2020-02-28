from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import csv


set_wind = Tk()
set_wind.title("Test Setup")                    # window title
set_wind.geometry('800x480')                    # window geometry
set_wind.configure(background='white')          # window background
frame = Frame(set_wind, background='white')         # frame bakground
frame.place(anchor='nw', relwidth=1, relheight=1)       # Frame placement

Label(frame, text="TEST SETUP", background='white', font='Arial 20 bold underline').place(anchor='n', relx=.5)


def openfile():         # opens file selection window and saves selected file to dictionary
    selected_file = filedialog.askopenfilename(title="Select a CSV File",       # opens file selector window
                                      filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))

    with open(selected_file, 'r', newline='') as setupfile:         # opens selected file
        setupfile_reader = csv.DictReader(setupfile)                # reads selected file to dictionary
        for row in setupfile_reader:
            print(row)
            # Need to save each value from the CSV file to instance variables of a class
    print(list)


Button(frame, text='Select Setup File to Read', font='Arial 12', bg='#80bfff', activebackground='#ccebff',
       height='3', width='30', command=openfile).place(anchor='n', relx=.5, rely=.15)




mainloop()