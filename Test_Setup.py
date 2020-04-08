from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import csv
try:
    from IOPi import IOPi
except ModuleNotFoundError:
    from test import Bus as IOPi

# initialize port directions for LED illumination
bus1 = IOPi(0x20)                                # I2C address (bus 1, board 1)
bus1.set_port_direction(0, 0x00)                 # 0: pins 1-8, 0x00: set port direction as output
bus1.set_port_direction(1, 0x00)                 # 1: pins 9-16, 0x00: set port direction as output
bus1.write_port(0, 0x00)                         # initially turn off all pins

bus2 = IOPi(0x21)                                # I2C address (bus 2, board 1)
bus2.set_port_direction(0, 0x00)                 # 0: pins 1-8, 0x00: set port direction as output
bus2.set_port_direction(1, 0x00)                 # 1: pins 9-16, 0x00: set port direction as output
bus2.write_port(0, 0x00)                         # initially turn off all pins

bus3 = IOPi(0x22)                                # I2C address (bus 1, board 2)
bus3.set_port_direction(0, 0x00)                 # 0: pins 1-8, 0x00: set port direction as output
bus3.set_port_direction(1, 0x00)                 # 1: pins 9-16, 0x00: set port direction as output
bus3.write_port(0, 0x00)                         # initially turn off all pins

bus4 = IOPi(0x23)                                # I2C address (bus 2, board 2)
bus4.set_port_direction(0, 0x00)                 # 0: pins 1-8, 0x00: set port direction as output
bus4.set_port_direction(1, 0x00)                 # 1: pins 9-16, 0x00: set port direction as output
bus4.write_port(0, 0x00)                         # initially turn off all pins


class TestSetup(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.map = {}  # initialize empty dictionary for pinout map

        # initializes dictionary to store barcode information
        self.barcodes = {}

        # initialize list to store only barcodes from setup file (used for comparison)
        self.only_codes = []

        # dictionary stores 4 different bus addresses
        self.buses = {1: bus1, 2: bus2, 3: bus3, 4: bus4}

        # dictionary maps each slot to a bus and pin
        with open('Pinout_Map.csv', 'r', newline='') as map_file:       # opens selected file for reading
            reader = csv.reader(map_file)   # reads selected file
            next(reader)                    # goes to second line of csv file

            for row in reader:
                self.map[row[0]] = {'bus': row[1], 'pin': row[2]}     # saves csv info to dictionary

        for case, key in self.map.items():
            key['bus'] = int(key['bus'])
            key['pin'] = int(key['pin'])

        self.prev_slot = '1'

        # function opens file selection window and saves selected csv file information into dictionaries
        def select_file():
            # opens file selector window
            selected_file = filedialog.askopenfilename(title="Select a CSV File", filetypes=(("CSV files", "*.csv"),
                                                                                             ("all files", "*.*")))

            with open(selected_file, 'r', newline='') as setup_file:        # opens selected file for reading
                setup_file_reader = csv.reader(setup_file)                  # reads selected file
                next(setup_file_reader)                                     # goes to second line of csv file

                for row in setup_file_reader:
                    self.barcodes[row[0]] = {'he': row[1], 'nrc': row[2], 'ab': row[3]}  # saves csv info to dictionary

            with open(selected_file, 'r', newline='') as temp_setup_file:  # opens selected file for reading
                temp_file_reader = csv.reader(temp_setup_file)
                next(temp_file_reader)                                     # goes to second line of csv file

                with open('temporary_file.csv', 'w', newline='') as temp_file:      # opens a temporary file used later
                    temp_file_writer = csv.writer(temp_file)               # creates a csv writer
                    for line in temp_file_reader:
                        temp_file_writer.writerow(line)                    # copies setup file to temporary file

            with open(selected_file, 'r', newline='') as setup_file:        # opens selected file for reading
                setup_file_reader = csv.reader(setup_file)                  # reads selected file
                next(setup_file_reader)                                     # goes to second line of csv file

                # saves only the barcodes from the setup file to a list (used in compare function)
                for row in setup_file_reader:
                    self.only_codes.append(row[1])
                    self.only_codes.append(row[2])
                    self.only_codes.append(row[3])

            # prompts user to scan and read barcode once setup file is selected
            Label(self, text="Setup file read.\nScan and read a slide to determine its corresponding case and slot:",
                  font='Arial 12 bold').place(anchor='n', relx=.5, rely=.375)

            # initializes barcode_entry variable as type: string
            barcode_entry = StringVar()

            # entry field for scanned barcode
            Entry(self, textvariable=barcode_entry, background='#BDBDBD', font='Arial 20', ).place(
                anchor='n', relx=.575, rely=.5, width='450', height='70')

            # button to read the scanned barcode, command calls 'compare' function
            Button(self, text='Read\nBarcode', font='Arial 12 bold', bg='#00cc66', activebackground='#80ffbf',
                   height='3', width='10', command=lambda: compare(barcode_entry.get())).place(anchor='n',
                                                                                               relx=.2, rely=.5)

            # prompts user to place slide in the correct slot depending on the barcode scanned
            def compare(barcode_entry):

                bus_number = self.map[self.prev_slot]['bus']  # determines bus number of current case
                pin_number = self.map[self.prev_slot]['pin']  # determines pin number of current case

                bus = self.buses[bus_number]    # determines which bus address to use
                bus.write_pin(pin_number, 0)     # turns OFF LED for previous slot

                for case, case_info in self.barcodes.items():            # loops through 'barcodes' dictionary

                    # checks to see if scanned barcode matches a value from csv file
                    if barcode_entry == case_info['he'] or barcode_entry == case_info['nrc']\
                            or barcode_entry == case_info['ab']:

                        Label(self, text="Place scanned slide in the illuminated slot.",
                              font='Arial 12 bold').place(anchor='n', relx=.5, rely=.7)
                        key_val = StringVar()
                        key_val.set(case)
                        Label(self, textvariable=key_val, font='Arial 12 bold').place(anchor='n', relx=.53,
                                                                                      rely=.75, width='40')
                        Label(self, text='Slot #:', font='Arial 12 bold').place(anchor='n', relx=.48, rely=.75)
                        bus_number = self.map[case]['bus']  # determines bus number of current case
                        pin_number = self.map[case]['pin']  # determines pin number of current case

                        bus = self.buses[bus_number]    # determines which bus address to use
                        bus.write_pin(pin_number, 1)     # turns ON LED for current slot

                        self.prev_slot = case   # save previous slot number to turn off for a new scan

                # displays if barcode scanned is not listed in setup file
                if barcode_entry not in self.only_codes:
                    Label(self, text='INVALID', font='Arial 12 bold').place(anchor='n', relx=.5, rely=.75, width='100')
                    messagebox.showerror(title="Invalid", message="This barcode is not listed in the setup file.\n"
                                                                  "Either choose a new setup file or select a slide\n"
                                                                  "that is listed in the setup file.")

        def back_page():
            bus_number = self.map[self.prev_slot]['bus']  # determines bus number of current case
            pin_number = self.map[self.prev_slot]['pin']  # determines pin number of current case

            bus = self.buses[bus_number]    # determines which bus address to use
            bus.write_pin(pin_number, 0)     # turns OFF LED for previous slot

            controller.show_frame("SetDatRand")

        def back_to_home():
            bus_number = self.map[self.prev_slot]['bus']  # determines bus number of current case
            pin_number = self.map[self.prev_slot]['pin']  # determines pin number of current case

            bus = self.buses[bus_number]    # determines which bus address to use
            bus.write_pin(pin_number, 0)     # turns OFF LED for previous slot
            controller.show_frame("StartPage")

        Label(self, text="TEST SETUP", font='Arial 20 bold underline').place(anchor='n', relx=0.5, rely=0.05)

        # button to select setup file, command calls 'select_file' function
        Button(self, text='Select Setup File', font='Arial 12 bold', bg='#80bfff', activebackground='#ccebff',
               height='3', width='30', command=lambda: select_file()).place(anchor='n', relx=.5, rely=.2)

        # button calls show_frame method and takes you page to Start Page
        Button(self, text="Back To Home", fg="black", bg="#81DAF5", font="Arial 14", width='12', height='1',
               command=back_to_home).place(relx=1.0, rely=1.0, anchor=SE)

        # button calls show_frame method and takes you back one page to SetDatRand
        Button(self, text="Back", fg="black", bg="#81DAF5", font="Arial 14", width='12', height='1',
               command=back_page).place(relx=0.8, rely=1.0, anchor=SE)


# need to figure how to run this module on its own

if __name__ == "__main__":
    app = Tk()
    app.mainloop()