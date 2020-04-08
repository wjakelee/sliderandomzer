from tkinter import *
import csv
import itertools
from Start_Page import StartPage
from Test_Intro_Page import TestIntro
from collections import defaultdict
from tkinter import messagebox
try:
    from IOPi import IOPi
except ModuleNotFoundError:
    from test import Bus as IOPi


# initializing port directions for LED illumination
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


# class is used here to run this page alone
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

        self.frames = {}                      # initializes a dictionary that will store different page frames
        self.pages = {'StartPage': StartPage, 'TestIntro': TestIntro, 'QuestionPage': QuestionPage}

        # loop creates a frame for each page
        for name, F in self.pages.items():                      # loops through dictionary 'pages'
            frame = F(container, self)                              # assigns iterated frame to a variable 'frame'
            frame.grid(row=0, column=0, sticky="nsew")              # frame positioning
            self.frames[name] = frame                               # adds each page frame to dictionary of frames

        self.show_frame("QuestionPage")              # calls show_frame method to raise StartPage frame when run

    def show_frame(self, page):
        frame = self.frames[page]               # selects frame to be raised, determined by button click
        frame.tkraise()                         # raises frame called


class QuestionPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.barcode_info = {}
        self.current_case_codes = {}
        self.flag_values = {}       # initialize empty dictionary for flagging cases
        self.map = {}               # initialize empty dictionary for pinout map

        self.next_number = 0        # initialization of attribute next_number, this value gets updated when next
                                    # case function executes

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

        # initialize empty dictionary to save test answers (empty values are called upon in next_case function)
        self.test_answers = defaultdict(dict)
        n_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                  '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35',
                  '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52',
                  '53', '54', '55', '56', '57', '58', '59', '60']
        for i in n_list:
            self.test_answers[i]['Q1'] = ' '
            self.test_answers[i]['Q2'] = ' '
            self.test_answers[i]['Q3'] = ' '
            self.test_answers[i]['Q4'] = ' '
            self.test_answers[i]['Q5'] = ' '
            self.test_answers[i]['Q6'] = ' '
            self.test_answers[i]['Comments'] = ' '
            self.flag_values[i] = 'Unflag'

        # reads randomization order from temporary_file.csv and begins test
        def start_test():

            Label(self, text='Test is in progress.', font='Arial 12',
                  bg='light gray').place(anchor='w', relx=0.03, rely=0.125, width='160', height='80')

            with open('temporary_file.csv', 'r', newline="") as temp_file:          # open temporary file
                reader = csv.reader(temp_file)
                order_list = []                              # initialize empty list
                for row in reader:
                    order_list.append(row[0])                 # creates an list with the randomization order
                case_order = itertools.cycle(order_list)        # allow cycle through list indefinitely
                self.next_number = next(case_order)             # first number in case order

            bus_number = self.map[self.next_number]['bus']  # determines bus number of current case
            pin_number = self.map[self.next_number]['pin']  # determines pin number of current case

            bus = self.buses[bus_number]    # determines which bus address to use
            bus.write_pin(pin_number, 1)     # turns ON LED for current slot

            def compare(entry):

                self.current_case_codes = {}

                with open('temporary_file.csv', 'r', newline="") as temp_file:  # open temporary file
                    reader = csv.reader(temp_file)
                    for row in reader:
                        # saves csv info to dictionary
                        self.barcode_info[row[0]] = {'he': row[1], 'nrc': row[2], 'ab': row[3]}

                # saves current case codes to its own dictionary
                self.current_case_codes[self.next_number] = self.barcode_info[self.next_number]

                # checks to see if scanned barcode matches current case codes
                if entry == self.current_case_codes[self.next_number]['he'] or entry ==\
                        self.current_case_codes[self.next_number]['nrc'] or entry ==\
                        self.current_case_codes[self.next_number]['ab']:
                    Label(self, text='Correct case selected:\n\n1. Evaluate all slides in case.'
                                     '\n2. Answer all questions.\n3. Save Answers.\n4. Press "next case" for'
                                     '\nnew case evaluation.', background='#BDBDBD', font='Arial 10',
                          justify=LEFT).place(anchor='w', relx=.03, rely=.5, width='230', height='130')

                # checks to see if scanned barcode does not match current case codes
                if entry != self.current_case_codes[self.next_number]['he'] and entry != \
                        self.current_case_codes[self.next_number]['nrc'] and entry !=\
                        self.current_case_codes[self.next_number]['ab']:
                    Label(self, text='Wrong case selected:\n\nPlease select the correct\n'
                                     '(illuminated) case and rescan\nall slides.',
                          background='#BDBDBD', font='Arial 10', justify=LEFT).place(anchor='w', relx=.03,
                                                                                     rely=.5, width='200',
                                                                                     height='130')

            # function saves answers to test_answers dictionary for each case
            def save_answers(ans_1, ans_2, ans_3, ans_4, ans_5, ans_6, comments):
                self.test_answers[self.next_number] = {'Q1': ans_1.get(), 'Q2': ans_2.get(), 'Q3': ans_3.get(),
                                                       'Q4': ans_4.get(), 'Q5': ans_5.get(), 'Q6': ans_6.get(),
                                                       'Comments':  comments.get()}

                messagebox.showinfo(title="Saved", message="Answers saved.")

            # displays next case number
            def next_case(flag, case_order, ans_1, ans_2, ans_3, ans_4, ans_5, ans_6, comments):

                # initial message to start scanning
                Label(self, text='Scan and read the barcode\nof each slide for the case\nshown above (illuminated).',
                      background='#BDBDBD', font='Arial 10', justify=LEFT).place(anchor='w', relx=.03, rely=.5,
                                                                                    width='230', height='130')

                bus_number = self.map[self.next_number]['bus']  # determines bus number of current case
                pin_number = self.map[self.next_number]['pin']  # determines pin number of current case

                bus = self.buses[bus_number]    # determines which bus address to use
                bus.write_pin(pin_number, 0)     # turns OFF LED for current slot

                self.next_number = next(case_order)        # next number in randomization order

                # displays previously saved answers for each case depending on which case is requested
                ans_1.set(self.test_answers[self.next_number]['Q1'])
                ans_2.set(self.test_answers[self.next_number]['Q2'])
                ans_3.set(self.test_answers[self.next_number]['Q3'])
                ans_4.set(self.test_answers[self.next_number]['Q4'])
                ans_5.set(self.test_answers[self.next_number]['Q5'])
                ans_6.set(self.test_answers[self.next_number]['Q6'])
                comments.set(self.test_answers[self.next_number]['Comments'])

                # set flag to correct setting for current case
                flag.set(self.flag_values[self.next_number])

                value = StringVar()                        # makes number variable type String
                value.set(self.next_number)                # sets number variable to next number in randomization order
                Label(self, textvariable=value, font='Arial 18',
                      background='#BDBDBD').place(anchor='w', relx=.15, rely=.3, width='35', height='50')

                bus_number = self.map[self.next_number]['bus']       # determines bus number of current case
                pin_number = self.map[self.next_number]['pin']       # determines pin number of current case

                bus = self.buses[bus_number]    # determines which bus address to use
                bus.write_pin(pin_number, 1)     # turns ON LED for current slot

            def flagging():
                self.flag_values[self.next_number] = 'Flag'

            def unflagging():
                self.flag_values[self.next_number] = 'Unflag'

            def end_test():

                def merge_dict(a, b):
                    a.update(b)
                    return a

                # saves answers to a temporary answer CSV file, this is used in the export button of Rand_and_Data.py
                fields = ['Case', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Comments']
                with open('previous_ans.csv', 'w', newline='') as prev_ans_file:  # opens selected file for reading
                    writer = csv.DictWriter(prev_ans_file, fields)
                    writer.writeheader()
                    for case, question in self.test_answers.items():
                        writer.writerow(merge_dict({'Case': case}, question))

                # show next frame
                controller.show_frame("ConfirmationPage")

            # initial message to start scanning
            Label(self, text='Scan and read the barcode\nof each slide for the case\nshown above (illuminated).',
                  background='#BDBDBD', font='Arial 10', justify=LEFT).place(anchor='w', relx=.03, rely=.5,
                                                                                 width='230', height='130')
            # initializes barcode_entry variable as type: string
            barcode_entry = StringVar()

            # entry field for scanned barcode
            Entry(self, textvariable=barcode_entry, background='#BDBDBD', font='Arial 14', bd=4).place(
                anchor='w', relx=.17, rely=.725, width='150', height='50')

            # button to read the scanned barcode, command calls 'compare' function
            Button(self, text='Read\nBarcode', font='Arial 12 bold', bg='#00cc66', activebackground='#80ffbf',
                   height='2', width='8', command=lambda: compare(barcode_entry.get())).place(anchor='w',
                                                                                              relx=.03, rely=.725)

            # label for question 1
            Label(self, text='1. H&E Acceptable?', font='Arial 12').place(anchor='w', relx=.385, rely=.075)

            ans_1 = StringVar()  # initialize entry variable for question 1
            ans_1.set(" ")
            Radiobutton(self, text='Yes', font='Arial 12 bold', variable=ans_1,
                        value='Yes').place(anchor='w', relx=0.7, rely=0.075)
            Radiobutton(self, text='No', font='Arial 12 bold', variable=ans_1,
                        value='No').place(anchor='w', relx=0.8, rely=0.075)
            Radiobutton(self, text='N/A', font='Arial 12 bold', variable=ans_1,
                        value='N/A').place(anchor='w', relx=0.9, rely=0.075)

            # label for question 2
            Label(self, text='2. Negative Control Acceptable?',
                  font='Arial 12').place(anchor='w', relx=.385, rely=.155)

            ans_2 = StringVar()  # initialize entry variable for question 2
            ans_2.set(" ")
            Radiobutton(self, text='Yes', font='Arial 12 bold', variable=ans_2,
                        value='Yes').place(anchor='w', relx=0.7, rely=.155)
            Radiobutton(self, text='No', font='Arial 12 bold', variable=ans_2,
                        value='No').place(anchor='w', relx=0.8, rely=.155)
            Radiobutton(self, text='N/A', font='Arial 12 bold', variable=ans_2,
                        value='N/A').place(anchor='w', relx=0.9, rely=.155)

            # label for question 3
            Label(self, text='3. Case Morphology Acceptable?',
                  font='Arial 12').place(anchor='w', relx=.385, rely=.235)

            ans_3 = StringVar()  # initialize entry variable for question 3
            ans_3.set(" ")
            Radiobutton(self, text='Yes', font='Arial 12 bold', variable=ans_3,
                        value='Yes').place(anchor='w', relx=0.7, rely=.235)
            Radiobutton(self, text='No', font='Arial 12 bold', variable=ans_3,
                        value='No').place(anchor='w', relx=0.8, rely=.235)
            Radiobutton(self, text='N/A', font='Arial 12 bold', variable=ans_3,
                        value='N/A').place(anchor='w', relx=0.9, rely=.235)

            # label for question 4
            Label(self, text='4. Background Acceptable?',
                  font='Arial 12').place(anchor='w', relx=.385, rely=.315)

            ans_4 = StringVar()  # initialize entry variable for question 4
            ans_4.set(" ")
            Radiobutton(self, text='Yes', font='Arial 12 bold', variable=ans_4,
                        value='Yes').place(anchor='w', relx=0.7, rely=.315)
            Radiobutton(self, text='No', font='Arial 12 bold', variable=ans_4,
                        value='No').place(anchor='w', relx=0.8, rely=.315)
            Radiobutton(self, text='N/A', font='Arial 12 bold', variable=ans_4,
                        value='N/A').place(anchor='w',  relx=0.9, rely=.315)

            # label for question 5
            Label(self, text='5. % Cell Staining (Raw Score, 0-100):',
                  font='Arial 12').place(anchor='w', relx=.385, rely=.395)

            ans_5 = StringVar()  # initialize entry variable for question 5
            # entry field for question 5
            Entry(self, textvariable=ans_5, background='#BDBDBD', bd=4, justify=CENTER,
                  font='Arial 12').place(anchor='w', relx=0.75, rely=0.395, width='120', height='35')

            # label for question 6
            Label(self, text='6. Case Status:',
                  font='Arial 12').place(anchor='w', relx=.385, rely=.475)

            ans_6 = StringVar()  # initialize entry variable for question 6
            ans_6.set(" ")
            Radiobutton(self, text='Positive', font='Arial 12 bold', variable=ans_6,
                        value='Positive').place(anchor='w', relx=0.55, rely=.475)
            Radiobutton(self, text='Negative', font='Arial 12 bold', variable=ans_6,
                        value='Negative').place(anchor='w', relx=0.7, rely=.475)
            Radiobutton(self, text='N/A', font='Arial 12 bold', variable=ans_6,
                        value='N/A').place(anchor='w', relx=0.85, rely=.475)

            # label for comments
            Label(self, text='7. Comments:',
                  font='Arial 12').place(anchor='w', relx=.385, rely=.555)

            comments = StringVar()
            # entry field for comments
            Entry(self, textvariable=comments, background='#BDBDBD', font='Arial 12', bd=4,
                  justify=LEFT).place(anchor='w', relx=.41, rely=.675, width='430', height='70')

            # Case number display
            Label(self, text='Case #', background='#BDBDBD',
                  font='Arial 18').place(anchor='w', relx=.03, rely=.3, width='100', height='50')

            value = StringVar()                       # makes number variable type String
            value.set(self.next_number)               # initial case number to be displayed
            Label(self, textvariable=value, font='Arial 18',
                  background='#BDBDBD').place(anchor='w', relx=.15, rely=.3, width='35', height='50')

            # button calls save_answers function
            Button(self, text='Save Answers', bg='#33adff', fg='black', font='Arial 16 bold',
                   command=lambda: save_answers(ans_1, ans_2, ans_3, ans_4, ans_5, ans_6,
                                                comments)).place(anchor='w', relx=0.725, rely=0.9,
                                                                 width='160', height='60')

            # Flag case number buttons
            flag = StringVar()
            flag.set("Unflag")
            Radiobutton(self, text='Flag', font='Arial 16 bold', fg='red', variable=flag,
                        command=flagging, value='Flag').place(anchor='w', relx=0.245, rely=.1)
            Radiobutton(self, text='Unflag', font='Arial 16 bold', variable=flag, command=unflagging,
                        value='Unflag').place(anchor='w', relx=0.245, rely=.2)

            # button calls end_test function
            Button(self, text='End Test', bg='#ff4d4d', fg='black', font='Arial 16 bold',
                   command=end_test).place(anchor='n', relx=0.5, rely=0.85, width='120', height='50')

            # button calls next_case function
            Button(self, text='Next Case', bg='#FF9F2A', fg='black',
                   font='Arial 16 bold', command=lambda: next_case(flag, case_order, ans_1, ans_2, ans_3, ans_4, ans_5,
                                                                   ans_6, comments)).place(anchor='w', relx=0.03,
                                                                                           rely=0.9, width='120',
                                                                                           height='60')

        # button calls start_test function
        Button(self, text='Start Test', bg='#47d147', fg='black', font='Arial 16 bold',
               command=start_test).place(anchor='w', relx=0.03, rely=0.125, width='120', height='80')


if __name__ == "__main__":
    app = Application()
    app.mainloop()
