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


class Data:
    def __init__(self, case, he, nrc, ab):
        self.case = case
        self.he = he
        self.nrc = nrc
        self.ab = ab


# function will compare scanned barcode to the barcodes saved from setup file
def compare():
    Label(frame, text="Place scanned slide in the illuminated slot. Slot #.", background='white',
          font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)


# function opens file selection and saves selected csv file information to dictionary
def selectfile():
    selected_file = filedialog.askopenfilename(title="Select a CSV File",       # opens file selector window
                    filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))

    dict = {}                                                       # initialize empty dictionary
    with open(selected_file, 'r', newline='') as setupfile:         # opens selected file
        setupfile_reader = csv.reader(setupfile)                    # reads selected file to dictionary
        next(setupfile_reader)                                      # goes to second line of csv file
        for row in setupfile_reader:
            dict[row[0]] = {'he': row[1], 'nrc': row[2], 'ab': row[3]}          # saves csv information to dictionary

    print(dict)

            # Need to save each value from the CSV file to instance variables of a class

    # asks user to scan and read barcode once setup file is selected
    Label(frame, text="Setup file read.\nScan and read a slide to determine its corresponding case and slot:",
          background='white', font='Arial 12 bold').place(anchor='n', relx=.5, rely=.325)

    barcode = StringVar()
    Entry(frame, textvariable=barcode, background='#e6e6e6', font='Arial 20', ).place(anchor='n', relx=.575,
            rely=.45, width='450', height='70')

    # button to read the scanned barcode, command calls 'compare' function
    Button(frame, text='Read\nBarcode', font='Arial 12 bold', bg='#00cc66', activebackground='#80ffbf',
           height='3', width='10', command=compare).place(anchor='n', relx=.2, rely=.45)


# button to select setup file, command calls 'selectfile' function
Button(frame, text='Select Setup File', font='Arial 12 bold', bg='#80bfff', activebackground='#ccebff',
       height='3', width='30', command=selectfile).place(anchor='n', relx=.5, rely=.15)



mainloop()