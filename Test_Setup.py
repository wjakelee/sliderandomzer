from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
# from IOPi import IOPi # (COMMENT  WHEN TESTING WITHOUT HARDWARE)
import csv


# initializing port directions for LED illumination (COMMENT LINES 11-25 WHEN TESTING WITHOUT HARDWARE)
# bus1 = IOPi(0x20)
# bus1.set_port_direction(0, 0x00)                 # set port direction
# bus1.write_port(0, 0x00)                         # write port
#
# bus2 = IOPi(0x21)
# bus2.set_port_direction(0, 0x00)                 # set port direction
# bus2.write_port(0, 0x00)                         # write port
#
# bus3 = IOPi(0x22)
# bus3.set_port_direction(0, 0x00)                 # set port direction
# bus3.write_port(0, 0x00)                         # write port
#
# bus4 = IOPi(0x23)
# bus4.set_port_direction(0, 0x00)                 # set port direction
# bus4.write_port(0, 0x00)                         # write port


class TestSetup(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # initializes dictionary to store barcode information
        self.barcodes = {}

        # initialize list to store only barcodes from setup file (used for comparison)
        self.only_codes = []

        # dictionary stores 4 different bus addresses (COMMENT WHEN TESTING WITHOUT HARDWARE)
        # self.buses = {1: IOPi(0x20), 2: IOPi(0x21), 3: IOPi(0x22), 4: IOPi(0x23)}

        self.test_buses = {1: '0x20', 2: '0x21', 3: '0x22', 4: '0x23'}  # COMMENT WHEN USING HARDWARE

        # dictionary maps each slot to a bus and pin (need to add the rest of the slots)
        self.map = {'1': {'bus': 1, 'pin': 1}, '2': {'bus': 1, 'pin': 2}, '3': {'bus': 1, 'pin': 3},
                    '4': {'bus': 1, 'pin': 4}, '5': {'bus': 1, 'pin': 5}, '6': {'bus': 1, 'pin': 6},
                    '7': {'bus': 1, 'pin': 7}, '8': {'bus': 1, 'pin': 8}, '9': {'bus': 1, 'pin': 9},
                    '10': {'bus': 1, 'pin': 10}, '11': {'bus': 1, 'pin': 11}, '12': {'bus': 1, 'pin': 12},
                    '13': {'bus': 1, 'pin': 13}, '14': {'bus': 1, 'pin': 14}, '15': {'bus': 1, 'pin': 15},
                    '16': {'bus': 1, 'pin': 16}, '17': {'bus': 2, 'pin': 1}, '18': {'bus': 2, 'pin': 2},
                    '19': {'bus': 2, 'pin': 3}, '20': {'bus': 2, 'pin': 4}, '21': {'bus': 2, 'pin': 5},
                    '22': {'bus': 2, 'pin': 6}, '23': {'bus': 2, 'pin': 7}, '24': {'bus': 2, 'pin': 8},
                    '25': {'bus': 2, 'pin': 9}, '26': {'bus': 2, 'pin': 10}, '27': {'bus': 2, 'pin': 11},
                    '28': {'bus': 2, 'pin': 12}, '29': {'bus': 2, 'pin': 13}, '30': {'bus': 2, 'pin': 14},
                    '31': {'bus': 2, 'pin': 15}, '32': {'bus': 2, 'pin': 16}, '33': {'bus': 3, 'pin': 1},
                    '34': {'bus': 3, 'pin': 2}, '35': {'bus': 3, 'pin': 3}, '36': {'bus': 3, 'pin': 4},
                    '37': {'bus': 3, 'pin': 5}, '38': {'bus': 3, 'pin': 6}, '39': {'bus': 3, 'pin': 7},
                    '40': {'bus': 3, 'pin': 8}, '41': {'bus': 3, 'pin': 9}, '42': {'bus': 3, 'pin': 10},
                    '43': {'bus': 3, 'pin': 11}, '44': {'bus': 3, 'pin': 12}, '45': {'bus': 3, 'pin': 13},
                    '46': {'bus': 3, 'pin': 14}, '47': {'bus': 3, 'pin': 15}, '48': {'bus': 3, 'pin': 16},
                    '49': {'bus': 4, 'pin': 1}, '50': {'bus': 4, 'pin': 2}, '51': {'bus': 4, 'pin': 3},
                    '52': {'bus': 4, 'pin': 4}, '53': {'bus': 4, 'pin': 5}, '54': {'bus': 4, 'pin': 6},
                    '55': {'bus': 4, 'pin': 7}, '56': {'bus': 4, 'pin': 8}, '57': {'bus': 4, 'pin': 9},
                    '58': {'bus': 4, 'pin': 10}, '59': {'bus': 4, 'pin': 11}, '60': {'bus': 4, 'pin': 12}}

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
            Entry(self, textvariable=barcode_entry, background='light grey', font='Arial 20', ).place(
                anchor='n', relx=.575, rely=.5, width='450', height='70')

            # button to read the scanned barcode, command calls 'compare' function
            Button(self, text='Read\nBarcode', font='Arial 12 bold', bg='#00cc66', activebackground='#80ffbf',
                   height='3', width='10', command=lambda: compare(barcode_entry.get())).place(anchor='n',
                                                                                               relx=.2, rely=.5)

            # prompts user to place slide in the correct slot depending on the barcode scanned
            def compare(barcode_entry):

                bus_number = self.map[self.prev_slot]['bus']  # determines bus number of current case
                pin_number = self.map[self.prev_slot]['pin']  # determines pin number of current case

                bus = self.test_buses[bus_number]  # COMMENT FOR TESTING WITH HARDWARE
                print(bus)  # COMMENT WHEN USING HARDWARE
                print(pin_number)  # COMMENT WHEN USING HARDWARE
                print('OFF\n')  # COMMENT WHEN USING HARDWARE

                # bus = self.buses[bus_number]    # determines which bus address to use (COMMENT WHEN TESTING WITHOUT HARDWARE)
                # bus.write_pin(pin_number, 0)     # turns OFF LED for previous slot (COMMENT WHEN TESTING WITHOUT HARDWARE)


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

                        bus = self.test_buses[bus_number]  # COMMENT FOR TESTING WITH HARDWARE
                        print(bus)  # COMMENT WHEN USING HARDWARE
                        print(pin_number)  # COMMENT WHEN USING HARDWARE
                        print('ON')  # COMMENT WHEN USING HARDWARE
                        print('-------')  # COMMENT WHEN USING HARDWARE

                        # bus = self.buses[bus_number]    # determines which bus address to use (COMMENT WHEN TESTING WITHOUT HARDWARE)
                        # bus.write_pin(pin_number, 1)     # turns ON LED for current slot (COMMENT WHEN TESTING WITHOUT HARDWARE)

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

            bus = self.test_buses[bus_number]  # COMMENT FOR TESTING WITH HARDWARE
            print(bus)  # COMMENT WHEN USING HARDWARE
            print(pin_number)  # COMMENT WHEN USING HARDWARE
            print('OFF\n')  # COMMENT WHEN USING HARDWARE

            # bus = self.buses[bus_number]    # determines which bus address to use (COMMENT WHEN TESTING WITHOUT HARDWARE)
            # bus.write_pin(pin_number, 0)     # turns OFF LED for previous slot (COMMENT WHEN TESTING WITHOUT HARDWARE)

            controller.show_frame("SetDatRand")

        def back_to_home():
            bus_number = self.map[self.prev_slot]['bus']  # determines bus number of current case
            pin_number = self.map[self.prev_slot]['pin']  # determines pin number of current case

            bus = self.test_buses[bus_number]  # COMMENT FOR TESTING WITH HARDWARE
            print(bus)  # COMMENT WHEN USING HARDWARE
            print(pin_number)  # COMMENT WHEN USING HARDWARE
            print('OFF\n')  # COMMENT WHEN USING HARDWARE

            # bus = self.buses[bus_number]    # determines which bus address to use (COMMENT WHEN TESTING WITHOUT HARDWARE)
            # bus.write_pin(pin_number, 0)     # turns OFF LED for previous slot (COMMENT WHEN TESTING WITHOUT HARDWARE)
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