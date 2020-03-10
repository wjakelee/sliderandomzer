from tkinter import *
from tkinter import filedialog
import csv


class Application(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Application")                               # window title
        self.geometry('800x480')                                # window geometry
        self.configure(background='white')                      # window background
        container = Frame(self, background='white')                 # creates a frame in tkinter
        container.place(anchor='nw', relwidth=1, relheight=1)       # location of frame covers entire window

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}                        # initializes a dictionary that will store different page frames

        for F in (StartPage, Login, SetDatRand, TestSetup):         # loops through page frames to add to dictionary
            frame = F(container, self)                              # assigns iterated frame to a variable 'frame'
            frame.grid(row=0, column=0, sticky="nsew")              # frame positioning
            self.frames[F] = frame                                  # adds each page frame frame to dictionary of frames

        self.show_frame(StartPage)              # calls show_frame method to raise StartPage frame when run

    def show_frame(self, page):
        frame = self.frames[page]               # selects frame to be raised, determined by button click
        frame.tkraise()                         # raises frame called


class StartPage(Frame):                         # start up / home page, class inherits Frame

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        Label(self, text="Please select an option below:", font='Arial 22 bold', bg="white").place(relx=0.5, rely=0.2,
                                                                                                   anchor='n')

        # Button takes you to take test page (still need to setup this page)
        Button(self, text="Take Test", fg="black", font='Arial 14 bold', width='20', height='5',
               bg="#33cc33").place(relx=0.3, rely=0.5, anchor=CENTER)

        # button calls show_frame method and raises to Login frame
        Button(self, text="Setup, DataFile,\nRandomization (Admin Only)", font='Arial 14 bold', width='30',
               height='5', fg="black", bg="#6699ff", command=lambda: controller.show_frame(Login)).place(
            relx=0.65, rely=0.5, anchor=CENTER)

        # Button exits desktop (doesnt do anything yet, may not actually need this button)
        Button(self, text="Exit to Desktop", font="Arial 14", fg="black", bg="#ff4d4d", width='15',
               height='2').place(relx=1.0, rely=1.0, anchor=SE)


class Login(Frame):  # Sample Login page

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # Function checks to see if the entered username/password are correct and calls show_frame module to raise
        # the SetDatRand frame
        def check_entry(username, password):
            if username == "admin" and password == "password":
                controller.show_frame(SetDatRand)                   # raises SetDatRand frame

        Label(self, text="Please enter the following information:", font='Arial 22 bold').place(relx=0.5, rely=0.2,
                                                                                                anchor='n')

        username = StringVar()
        password = StringVar()

        Label(self, text="Username:", font='Arial 16 bold').place(relx=0.5, rely=0.35, anchor='n')
        Entry(self, textvariable=username).place(relx=0.5, rely=0.4, anchor='n')                # username entry

        Label(self, text="Password:", font='Arial 16 bold').place(relx=0.5, rely=0.55, anchor='n')
        Entry(self, show="*", textvariable=password).place(relx=0.5, rely=0.6, anchor='n')      # password entry

        # button commands check_entry function
        Button(self, text="Enter", font='Arial 16 bold', fg="black", bg="grey", height='3', width='10',
               command=lambda: check_entry(username.get(), password.get())).place(relx=0.5, rely=0.7, anchor='n')

        # button calls show_frame method and takes you page to Start Page
        Button(self, text="Back To Home", fg="black", bg="#81DAF5", font="Arial 14", width='15', height='2',
               command=lambda: controller.show_frame(StartPage)).place(relx=1.0, rely=1.0, anchor=SE)


class SetDatRand(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # button calls show_frame method and takes you to TestSetup page
        Button(self, text="Test Setup", fg="black", font='Arial 14 bold', width='25', height='3',
               bg="#01DF3A", command=lambda: controller.show_frame(TestSetup)).place(relx=0.5, rely=0.25, anchor=CENTER)

        # button takes you to Data File and Randomization page (still need to setup)
        Button(self, text="Data File & Randomization", font='Arial 14 bold', width='25', height='3', fg="black",
               bg="#2E9AFE").place(relx=0.5, rely=0.5, anchor=CENTER)

        # button calls show_frame method and takes you to Start Page
        Button(self, text="Back To Home", fg="black", bg="#81DAF5", font="Arial 14", width='15', height='2',
               command=lambda: controller.show_frame(StartPage)).place(relx=1.0, rely=1.0, anchor=SE)


class TestSetup(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        Label(self, text="TEST SETUP", background='white', font='Arial 20 bold underline').place(anchor='n', relx=.5)

        # initializes two dictionaries to store barcode information
        cases = {}
        barcodes = {}

        # function opens file selection window and saves selected csv file information into dictionaries
        def select_file(cases, barcodes):
            # opens file selector window
            selected_file = filedialog.askopenfilename(title="Select a CSV File", filetypes=(("CSV files", "*.csv"),
                                                                                             ("all files", "*.*")))

            with open(selected_file, 'r', newline='') as setup_file:        # opens selected file for reading
                setup_file_reader = csv.reader(setup_file)                  # reads selected file
                next(setup_file_reader)                                     # goes to second line of csv file
                for row in setup_file_reader:
                    cases[row[0]] = {'he': row[1], 'nrc': row[2], 'ab': row[3]}     # saves csv info to dictionary
                    barcodes[row[0]] = {row[1]: 'he', row[2]: 'nrc', row[3]: 'ab'}  # saves csv info to 2nd dictionary

            # prompts user to scan and read barcode once setup file is selected
            Label(self, text="Setup file read.\nScan and read a slide to determine its corresponding case and slot:",
                  background='white', font='Arial 12 bold').place(anchor='n', relx=.5, rely=.325)

            # prompts user to place slide in the correct slot depending on the barcode scanned
            def compare(barcode_entry, barcodes):

                for case, case_info in barcodes.items():            # loops through 'barcodes' dictionary
                    for key in case_info:
                        if barcode_entry == key:        # checks to see if scanned barcode matches a value from csv file
                            Label(self, text="Place scanned slide in the illuminated slot.", background='white',
                                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.65)
                            key_val = StringVar()
                            key_val.set(case)
                            Label(self, textvariable=key_val, font='Arial 12 bold').place(anchor='n', relx=.52,
                                                                                          rely=.7)
                            Label(self, text='Slot #:', font='Arial 12 bold').place(anchor='n', relx=.48, rely=.7)

            # initializes barcode_entry variable as type: string
            barcode_entry = StringVar()

            # entry field for scanned barcode
            Entry(self, textvariable=barcode_entry, background='#e6e6e6', font='Arial 20', ).place(
                anchor='n', relx=.575, rely=.45, width='450', height='70')

            # button to read the scanned barcode, command calls 'compare' function
            Button(self, text='Read\nBarcode', font='Arial 12 bold', bg='#00cc66', activebackground='#80ffbf',
                   height='3', width='10', command=lambda: compare(barcode_entry.get(), barcodes)).place(anchor='n',
                                                                                                         relx=.2,
                                                                                                         rely=.45)

        # button to select setup file, command calls 'select_file' function
        Button(self, text='Select Setup File', font='Arial 12 bold', bg='#80bfff', activebackground='#ccebff',
               height='3', width='30', command=lambda: select_file(cases, barcodes)).place(anchor='n', relx=.5,
                                                                                           rely=.15)
        # button calls show_frame method and takes you page to Start Page
        Button(self, text="Back To Home", fg="black", bg="#81DAF5", font="Arial 14", width='15', height='2',
               command=lambda: controller.show_frame(StartPage)).place(relx=1.0, rely=1.0, anchor=SE)


app = Application()
app.mainloop()
