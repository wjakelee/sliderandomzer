from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import csv


set_wind = Tk()
set_wind.title("Test Setup")                    # window title
set_wind.geometry('800x480')                    # window geometry
set_wind.configure(background='white')          # window background
frame = Frame(set_wind, background='white')         # frame background
frame.place(anchor='nw', relwidth=1, relheight=1)       # Frame placement

Label(frame, text="TEST SETUP", background='white', font='Arial 20 bold underline').place(anchor='n', relx=.5)


# class Data:
#     def __init__(self, he, nrc, ab):
#         self.he = he
#         self.nrc = nrc
#         self.ab = ab


cases = {}
barcodes = {}


# function opens file selection window and saves selected csv file information into dictionaries
def select_file(cases, barcodes):
    # opens file selector window
    selected_file = filedialog.askopenfilename(title="Select a CSV File", filetypes=(("CSV files", "*.csv"),
                                                                                     ("all files", "*.*")))

    with open(selected_file, 'r', newline='') as setup_file:                     # opens selected file for reading
        setup_file_reader = csv.reader(setup_file)                                # reads selected file
        next(setup_file_reader)                                                  # goes to second line of csv file
        for row in setup_file_reader:
            cases[row[0]] = {'he': row[1], 'nrc': row[2], 'ab': row[3]}         # saves csv info to dictionary
            barcodes[row[0]] = {row[1]: 'he', row[2]: 'nrc', row[3]: 'ab'}      # saves csv info to 2nd dictionary

    # prompts user to scan and read barcode once setup file is selected
    Label(frame, text="Setup file read.\nScan and read a slide to determine its corresponding case and slot:",
          background='white', font='Arial 12 bold').place(anchor='n', relx=.5, rely=.325)

    # prompts user to place slide in the correct slot depending on the barcode scanned
    def compare(barcode_entry, barcodes):

        for case, case_info in barcodes.items():      # loops through 'barcodes' dictionary
            for key in case_info:
                if barcode_entry == key:              # checks to see if scanned barcode matches a value from csv file
                    Label(frame, text="Place scanned slide in the illuminated slot.", background='white',
                          font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
                    key_val = StringVar()
                    key_val.set(key)
                    Label(frame, textvariable=key_val, font='Arial 12 bold').place(anchor='n', relx=.52, rely=.7)
                    Label(frame, text='Slot #:', font='Arial 12 bold').place(anchor='n', relx=.48, rely=.7)

    # initializes barcode_entry variable as type: string
    barcode_entry = StringVar()

    # entry field for scanned barcode
    Entry(frame, textvariable=barcode_entry, background='#e6e6e6', font='Arial 20', ).place(
        anchor='n', relx=.575, rely=.45, width='450', height='70')

    # button to read the scanned barcode, command calls 'compare' function
    Button(frame, text='Read\nBarcode', font='Arial 12 bold', bg='#00cc66', activebackground='#80ffbf',
           height='3', width='10', command=lambda: compare(barcode_entry.get(), barcodes)).place(anchor='n', relx=.2, rely=.45)


# button to select setup file, command calls 'select_file' function
Button(frame, text='Select Setup File', font='Arial 12 bold', bg='#80bfff', activebackground='#ccebff',
       height='3', width='30', command=lambda: select_file(cases, barcodes)).place(anchor='n', relx=.5, rely=.15)


mainloop()