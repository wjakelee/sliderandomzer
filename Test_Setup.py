from tkinter import *
from tkinter import filedialog
import csv

# research running this module on its own, for now use dummy app


class TestSetup(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        Label(self, text="TEST SETUP", background='white', font='Arial 20 bold underline').place(anchor='n', relx=.5)

        # button to select setup file, command calls 'select_file' function
        Button(self, text='Select Setup File', font='Arial 12 bold', bg='#80bfff', activebackground='#ccebff',
               height='3', width='30', command=lambda: select_file(cases, barcodes)).place(anchor='n', relx=.5,
                                                                                           rely=.15)
        # button calls show_frame method and takes you page to Start Page
        Button(self, text="Back To Home", fg="black", bg="#81DAF5", font="Arial 14", width='15', height='2',
               command=lambda: controller.show_frame("StarPage")).place(relx=1.0, rely=1.0, anchor=SE)

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

# need to figure how to run this module on its own

if __name__ == "__main__":
    app = Tk()
    app.mainloop()