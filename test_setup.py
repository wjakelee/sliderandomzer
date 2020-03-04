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


# class used to store barcode information for each case
class Data:
    def __init__(self, he, nrc, ab):
        self.he = he
        self.nrc = nrc
        self.ab = ab


# initialize instance variables of class 'Data'
# this must be done since the barcode information for each case is referenced in the 'compare' function
case1 = Data(0, 0, 0)
case2 = Data(0, 0, 0)
case3 = Data(0, 0, 0)
case4 = Data(0, 0, 0)
case5 = Data(0, 0, 0)
case6 = Data(0, 0, 0)
case7 = Data(0, 0, 0)
case8 = Data(0, 0, 0)
case9 = Data(0, 0, 0)
case10 = Data(0, 0, 0)
case11 = Data(0, 0, 0)
case12 = Data(0, 0, 0)
case13 = Data(0, 0, 0)
case14 = Data(0, 0, 0)
case15 = Data(0, 0, 0)
case16 = Data(0, 0, 0)
case17 = Data(0, 0, 0)
case18 = Data(0, 0, 0)
case19 = Data(0, 0, 0)
case20 = Data(0, 0, 0)
case21 = Data(0, 0, 0)
case22 = Data(0, 0, 0)
case23 = Data(0, 0, 0)
case24 = Data(0, 0, 0)
case25 = Data(0, 0, 0)
case26 = Data(0, 0, 0)
case27 = Data(0, 0, 0)
case28 = Data(0, 0, 0)
case29 = Data(0, 0, 0)
case30 = Data(0, 0, 0)
case31 = Data(0, 0, 0)
case32 = Data(0, 0, 0)
case33 = Data(0, 0, 0)
case34 = Data(0, 0, 0)
case35 = Data(0, 0, 0)
case36 = Data(0, 0, 0)
case37 = Data(0, 0, 0)
case38 = Data(0, 0, 0)
case39 = Data(0, 0, 0)
case40 = Data(0, 0, 0)
case41 = Data(0, 0, 0)
case42 = Data(0, 0, 0)
case43 = Data(0, 0, 0)
case44 = Data(0, 0, 0)
case45 = Data(0, 0, 0)
case46 = Data(0, 0, 0)
case47 = Data(0, 0, 0)
case48 = Data(0, 0, 0)
case49 = Data(0, 0, 0)
case50 = Data(0, 0, 0)
case51 = Data(0, 0, 0)
case52 = Data(0, 0, 0)
case53 = Data(0, 0, 0)
case54 = Data(0, 0, 0)
case55 = Data(0, 0, 0)
case56 = Data(0, 0, 0)
case57 = Data(0, 0, 0)
case58 = Data(0, 0, 0)
case59 = Data(0, 0, 0)
case60 = Data(0, 0, 0)


# function opens file selection window and saves selected csv file information objects of the class 'Data'
def selectfile():
    global case1, case2, case3, case4, case5, case6, case7, case8, case9, case10, case11, case12, case13, case14,\
        case15, case16, case17, case18, case19, case20, case21, case22, case23, case24, case25, case26, case27, \
        case28, case29, case30, case31, case32, case33, case34, case35, case36, case37, case38, case39, case40, \
        case41, case42, case43, case44, case45, case46, case47, case48, case49, case50, case51, case52, case53, \
        case54, case55, case56, case57, case58, case59, case60

    # opens file selector window
    selected_file = filedialog.askopenfilename(title="Select a CSV File", filetypes=(("CSV files", "*.csv"),
                                                                                     ("all files", "*.*")))

    with open(selected_file, 'r', newline='') as setupfile:                     # opens selected file for reading
        file_reader = csv.DictReader(setupfile)                                 # reads selected file as dictionary

        # loops through csv file and stores barcode information for each case in attributes of the class 'Data'
        for row in file_reader:
            if row['case'] == '1':
                case1 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '2':
                case2 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '3':
                case3 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '4':
                case4 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '5':
                case5 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '6':
                case6 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '7':
                case7 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '8':
                case8 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '9':
                case9 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '10':
                case10 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '11':
                case11 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '12':
                case12 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '13':
                case13 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '14':
                case14 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '15':
                case15 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '16':
                case16 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '17':
                case17 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '18':
                case18 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '19':
                case19 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '20':
                case20 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '21':
                case21 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '22':
                case22 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '23':
                case23 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '24':
                case24 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '25':
                case25 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '26':
                case26 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '27':
                case27 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '28':
                case28 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '29':
                case29 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '30':
                case30 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '31':
                case31 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '32':
                case32 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '33':
                case33 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '34':
                case34 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '35':
                case35 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '36':
                case36 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '37':
                case37 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '38':
                case38 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '39':
                case39 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '40':
                case40 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '41':
                case41 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '42':
                case42 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '43':
                case43 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '44':
                case44 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '45':
                case45 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '46':
                case46 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '47':
                case47 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '48':
                case48 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '49':
                case49 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '50':
                case50 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '51':
                case51 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '52':
                case52 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '53':
                case53 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '54':
                case54 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '55':
                case55 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '56':
                case56 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '57':
                case57 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '58':
                case58 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '59':
                case59 = Data(row['he'], row['nrc'], row['ab'])
            if row['case'] == '60':
                case60 = Data(row['he'], row['nrc'], row['ab'])

    # prompts user to scan and read barcode once setup file is selected
    Label(frame, text="Setup file read.\nScan and read a slide to determine its corresponding case and slot:",
          background='white', font='Arial 12 bold').place(anchor='n', relx=.5, rely=.325)

    # function compares scanned barcode to the instance variables saved class 'Data'
    # prompts user to place slide in the correct slot depending on the barcode scanned
    def compare(barcode_entry):
        if barcode_entry == case1.he or barcode_entry == case1.nrc or barcode_entry == case1.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #1.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case2.he or barcode_entry == case2.nrc or barcode_entry == case2.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #2.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case3.he or barcode_entry == case3.nrc or barcode_entry == case3.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #3.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case4.he or barcode_entry == case4.nrc or barcode_entry == case4.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #4.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case5.he or barcode_entry == case5.nrc or barcode_entry == case5.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #5.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case6.he or barcode_entry == case6.nrc or barcode_entry == case6.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #6.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case7.he or barcode_entry == case7.nrc or barcode_entry == case7.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #7.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case8.he or barcode_entry == case8.nrc or barcode_entry == case8.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #8.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case9.he or barcode_entry == case9.nrc or barcode_entry == case9.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #9.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case10.he or barcode_entry == case10.nrc or barcode_entry == case10.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #10.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case11.he or barcode_entry == case11.nrc or barcode_entry == case11.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #11.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case12.he or barcode_entry == case12.nrc or barcode_entry == case12.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #12.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case13.he or barcode_entry == case13.nrc or barcode_entry == case13.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #13.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case14.he or barcode_entry == case14.nrc or barcode_entry == case14.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #14.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case15.he or barcode_entry == case15.nrc or barcode_entry == case15.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #15.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case16.he or barcode_entry == case16.nrc or barcode_entry == case16.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #16.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case17.he or barcode_entry == case17.nrc or barcode_entry == case17.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #17.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case18.he or barcode_entry == case18.nrc or barcode_entry == case18.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #18.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case19.he or barcode_entry == case19.nrc or barcode_entry == case19.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #19.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case20.he or barcode_entry == case20.nrc or barcode_entry == case20.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #20.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case21.he or barcode_entry == case21.nrc or barcode_entry == case21.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #21.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case22.he or barcode_entry == case22.nrc or barcode_entry == case22.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #22.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case23.he or barcode_entry == case23.nrc or barcode_entry == case23.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #23.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case24.he or barcode_entry == case24.nrc or barcode_entry == case24.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #24.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case25.he or barcode_entry == case25.nrc or barcode_entry == case25.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #25.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case26.he or barcode_entry == case26.nrc or barcode_entry == case26.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #26.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case27.he or barcode_entry == case27.nrc or barcode_entry == case27.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #27.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case28.he or barcode_entry == case28.nrc or barcode_entry == case28.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #28.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case29.he or barcode_entry == case29.nrc or barcode_entry == case29.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #29.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
        if barcode_entry == case30.he or barcode_entry == case30.nrc or barcode_entry == case30.ab:
            Label(frame, text="Place scanned slide in the illuminated slot. Slot #30.", background='white',
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)

    barcode_entry = StringVar()         # initializes barcode_entry variable as type: string
    # entry field for scanned barcode
    Entry(frame, textvariable=barcode_entry, background='#e6e6e6', font='Arial 20', ).place(
        anchor='n', relx=.575, rely=.45, width='450', height='70')

    # button to read the scanned barcode, command calls 'compare' function
    Button(frame, text='Read\nBarcode', font='Arial 12 bold', bg='#00cc66', activebackground='#80ffbf',
           height='3', width='10', command=lambda: compare(barcode_entry.get())).place(anchor='n', relx=.2, rely=.45)


# button to select setup file, command calls 'selectfile' function
Button(frame, text='Select Setup File', font='Arial 12 bold', bg='#80bfff', activebackground='#ccebff',
       height='3', width='30', command=selectfile).place(anchor='n', relx=.5, rely=.15)


mainloop()