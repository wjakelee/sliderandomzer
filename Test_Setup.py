from tkinter import *
from tkinter import filedialog
import csv

# research running this module on its own, for now use dummy app


class TestSetup(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        Label(self, text="TEST SETUP", font='Arial 20 bold underline').place(anchor='n', relx=0.5, rely=0.05)

        # button to select setup file, command calls 'select_file' function
        Button(self, text='Select Setup File', font='Arial 12 bold', bg='#80bfff', activebackground='#ccebff',
               height='3', width='30', command=lambda: select_file()).place(anchor='n', relx=.5, rely=.2)

        # button calls show_frame method and takes you page to Start Page
        Button(self, text="Back To Home", fg="black", bg="#81DAF5", font="Arial 14", width='12', height='1',
               command=lambda: controller.show_frame("StartPage")).place(relx=1.0, rely=1.0, anchor=SE)

        # button calls show_frame method and takes you back one page to SetDatRand
        Button(self, text="Back", fg="black", bg="#81DAF5", font="Arial 14", width='12', height='1',
               command=lambda: controller.show_frame("SetDatRand")).place(relx=0.8, rely=1.0, anchor=SE)

        # initializes dictionary to store barcode information
        self.barcodes = {}

        # function opens file selection window and saves selected csv file information into dictionaries
        def select_file():
            # opens file selector window
            selected_file = filedialog.askopenfilename(title="Select a CSV File", filetypes=(("CSV files", "*.csv"),
                                                                                             ("all files", "*.*")))

            with open(selected_file, 'r', newline='') as setup_file:        # opens selected file for reading
                setup_file_reader = csv.reader(setup_file)                  # reads selected file
                next(setup_file_reader)                                     # goes to second line of csv file

                for row in setup_file_reader:
                    self.barcodes[row[0]] = {row[1]: 'he', row[2]: 'nrc', row[3]: 'ab'}  # saves csv info to dictionary

            with open(selected_file, 'r', newline='') as temp_setup_file:  # opens selected file for reading
                temp_file_reader = csv.reader(temp_setup_file)
                next(temp_file_reader)                                     # goes to second line of csv file

                with open('temporary_file.csv', 'w', newline='') as temp_file:      # opens a temporary file used later
                    temp_file_writer = csv.writer(temp_file)               # creates a csv writer
                    for line in temp_file_reader:
                        temp_file_writer.writerow(line)                    # copies setup file to temporary file

            # prompts user to scan and read barcode once setup file is selected
            Label(self, text="Setup file read.\nScan and read a slide to determine its corresponding case and slot:",
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.375)

            # initializes barcode_entry variable as type: string
            barcode_entry = StringVar()

            # entry field for scanned barcode
            Entry(self, textvariable=barcode_entry, background='light grey', font='Arial 20', ).place(
                anchor='n', relx=.575, rely=.5, width='450', height='70')

            # button to read the scanned barcode, command calls 'compare' function
            Button(self, text='Read\nBarcode', font='Arial 12 bold', bg='#00cc66', activebackground='#80ffbf',
                   height='3', width='10', command=lambda: compare(barcode_entry.get())).place(anchor='n',
                                                                                               relx=.2, rely=.5)

            # prompts user to place slide in the correct slot depending on the barcode scanned
            def compare(barcode_entry):

                for case, case_info in self.barcodes.items():            # loops through 'barcodes' dictionary
                    for key in case_info:
                        if barcode_entry == key:        # checks to see if scanned barcode matches a value from csv file
                            Label(self, text="Place scanned slide in the illuminated slot.",
                                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.7)
                            key_val = StringVar()
                            key_val.set(case)
                            Label(self, textvariable=key_val, font='Arial 12 bold').place(anchor='n', relx=.52,
                                                                                          rely=.75)
                            Label(self, text='Slot #:', font='Arial 12 bold').place(anchor='n', relx=.48, rely=.75)


# need to figure how to run this module on its own

if __name__ == "__main__":
    app = Tk()
    app.mainloop()