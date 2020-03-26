from tkinter import *
# from IOPi import IOPi
import csv
import itertools
from Start_Page import StartPage
from Test_Intro_Page import TestIntro


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

        self.next_number = 0        # initialization of attribute next_number, this value gets updated when next
                                    # case function executes

        # initialize empty dictionary to save test answers (empty values are called upon in next_case function)
        self.test_answers = {'1': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '2': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '3': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '4': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '5': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '6': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '7': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '8': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '9': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '10': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '11': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '12': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '13': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '14': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '15': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '16': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '17': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '18': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '19': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '20': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '21': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '22': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '23': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '24': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '25': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '26': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '27': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '28': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '29': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '30': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '31': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '32': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '33': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '34': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '35': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '36': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '37': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '38': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '39': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '40': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '41': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '42': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '43': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '44': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '45': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '46': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '47': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '48': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '49': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '50': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '51': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '52': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '53': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '54': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '55': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '56': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '57': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '58': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '59': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''},
                             '60': {'Q1': '', 'Q2': '', 'Q3': '', 'Q4': '', 'Q5': '', 'Q6': '', 'Comments': ''}}


        # reads randomization order from temporary_file.csv and begins test
        def start_test():

            with open('temporary_file.csv', 'r', newline="") as temp_file:          # open temporary file
                reader = csv.reader(temp_file)
                order_list = []                              # initialize empty list
                for row in reader:
                    order_list.append(row[0])                 # creates an list with the randomization order
                case_order = itertools.cycle(order_list)        # allow cycle through list indefinitely
                self.next_number = next(case_order)             # first number in case order

            # function saves answers to test_answers dictionary for each case
            def save_answers(ans_1, ans_2, ans_3, ans_4, ans_5, ans_6, comments):
                self.test_answers[self.next_number] = {'Q1': ans_1.get(), 'Q2': ans_2.get(), 'Q3': ans_3.get(), 'Q4': ans_4.get(),
                                                       'Q5': ans_5.get(), 'Q6': ans_6.get(), 'Comments':  comments.get()}

                print(self.test_answers)

            # displays next case number
            def next_case(case_order, ans_1, ans_2, ans_3, ans_4, ans_5, ans_6, comments):

                self.next_number = next(case_order)        # next number in randomization order

                ans_1.set(self.test_answers[self.next_number]['Q1'])
                ans_2.set(self.test_answers[self.next_number]['Q2'])
                ans_3.set(self.test_answers[self.next_number]['Q3'])
                ans_4.set(self.test_answers[self.next_number]['Q4'])
                ans_5.set(self.test_answers[self.next_number]['Q5'])
                ans_6.set(self.test_answers[self.next_number]['Q6'])
                comments.set(self.test_answers[self.next_number]['Comments'])

                value = StringVar()                        # makes number variable type String
                value.set(self.next_number)                # sets number variable to next number in randomization order
                Label(self, textvariable=value, font='Arial 18',
                      background='light gray').place(anchor='w', relx=.15, rely=.3, width='35', height='50')

                # # dictionary stores 4 different bus addresses
                # buses = {'1': IOPi(0x21), '2': IOPi(0x22), '3': IOPi(0x23), '4': IOPi(0x24)}
                # # dictionary maps each slot to a bus and pin (need to add the rest of the slots)
                # map = {1: {'bus': 1, 'pin': 1}, 2: {'bus': 1, 'pin': 2}, 3: {'bus': 1, 'pin': 3},
                #        4: {'bus': 1, 'pin': 4}, 5: {'bus': 1, 'pin': 5}, 6: {'bus': 1, 'pin': 6},
                #        7: {'bus': 1, 'pin': 7}, 8: {'bus': 1, 'pin': 8}, 9: {'bus': 1, 'pin': 9},
                #        10: {'bus': 1, 'pin': 10}, 11: {'bus': 1, 'pin': 11}, 12: {'bus': 1, 'pin': 12},
                #        13: {'bus': 1, 'pin': 13}, 14: {'bus': 1, 'pin': 14}, 15: {'bus': 1, 'pin': 15},
                #        16: {'bus': 1, 'pin': 16}}
                #
                # bus_number = map[self.next_number]['bus']       # determines bus number of current case
                # pin_number = map[self.next_number]['pin']       # determines pin number of current case
                # bus = buses[bus_number]                         # determines which bus address to use
                # bus.set_port_direction(0, 0x00)                 # set port direction
                # bus.write_port(0, 0x00)                         # write port
                # bus.write_pin(pin_number, 1)                    # turns on LED for current slot

            # label for question 1
            Label(self, text='1. H&E Acceptable? (Yes/No)',
                  font='Arial 12').place(anchor='w', relx=.4, rely=.1)

            ans_1 = StringVar()  # initialize entry variable for question 1
            # entry field for question 1
            Entry(self, textvariable=ans_1, background='light grey',
                  font='Arial 12').place(anchor='w', relx=0.7, rely=0.1, width='100')

            # label for question 2
            Label(self, text='2. Negative Control Acceptable? (Yes/No)',
                  font='Arial 12').place(anchor='w', relx=.4, rely=.17)

            ans_2 = StringVar()  # initialize entry variable for question 2
            # entry field for question 2
            Entry(self, textvariable=ans_2, background='light grey',
                  font='Arial 12').place(anchor='w', relx=0.8, rely=0.17, width='100')

            # label for question 3
            Label(self, text='3. Case Morphology Acceptable? (Yes/No)',
                  font='Arial 12').place(anchor='w', relx=.4, rely=.24)

            ans_3 = StringVar()  # initialize entry variable for question 3
            # entry field for question 3
            Entry(self, textvariable=ans_3, background='light grey',
                  font='Arial 12').place(anchor='w', relx=0.8, rely=0.24, width='100')

            # label for question 4
            Label(self, text='4. Background Acceptable? (Yes/No)',
                  font='Arial 12').place(anchor='w', relx=.4, rely=.31)

            ans_4 = StringVar()  # initialize entry variable for question 4
            # entry field for question 4
            Entry(self, textvariable=ans_4, background='light grey',
                  font='Arial 12').place(anchor='w', relx=0.75, rely=0.31, width='100')

            # label for question 5
            Label(self, text='5. % Cell Staining (Raw Score, 0-100):',
                  font='Arial 12').place(anchor='w', relx=.4, rely=.38)

            ans_5 = StringVar()  # initialize entry variable for question 5
            # entry field for question 5
            Entry(self, textvariable=ans_5, background='light grey',
                  font='Arial 12').place(anchor='w', relx=0.75, rely=0.38, width='100')

            # label for question 6
            Label(self, text='6. Case Status (Pos/Neg):',
                  font='Arial 12').place(anchor='w', relx=.4, rely=.45)

            ans_6 = StringVar()  # initialize entry variable for question 6
            # entry field for question 6
            Entry(self, textvariable=ans_6, background='light grey',
                  font='Arial 12').place(anchor='w', relx=0.65, rely=0.45, width='100')

            # label for comments
            Label(self, text='7. Comments:',
                  font='Arial 12').place(anchor='w', relx=.4, rely=.52)

            comments = StringVar()
            # entry field for comments
            Entry(self, textvariable=comments, background='light grey', font='Arial 12',
                  justify=LEFT).place(anchor='w', relx=.41, rely=.7, width='430', height='120')

            # Case number display
            Label(self, text='Case #', background='light gray',
                  font='Arial 18').place(anchor='w', relx=.03, rely=.3, width='100', height='50')

            value = StringVar()                       # makes number variable type String
            value.set(self.next_number)               # initial case number to be displayed
            Label(self, textvariable=value, font='Arial 18',
                  background='light gray').place(anchor='w', relx=.15, rely=.3, width='35', height='50')

            # instructional display
            Label(self, text='1. Evaluate all slides in case.\n2. Answer all questions.'
                             '\n3. Save Answers.\n4. Press "next case" for\nnew case evaluation.',
                  background='light gray', font='Arial 10', justify=LEFT).place(anchor='w', relx=.03, rely=.5,
                                                                                width='200', height='120')

            # button calls save_answers function to save the first case answers only
            Button(self, text='Save Answers', bg='#33adff', fg='black', font='Arial 16 bold',
                   command=lambda: save_answers(ans_1, ans_2, ans_3, ans_4, ans_5, ans_6,
                                                comments)).place(anchor='w', relx=0.725, rely=0.9,
                                                                 width='160', height='40')

            # button calls next_case function
            Button(self, text='Next Case', bg='#bfbfbf', fg='black',
                   font='Arial 16 bold', command=lambda: next_case(case_order, ans_1, ans_2, ans_3, ans_4, ans_5, ans_6, comments)).place(anchor='w', relx=0.03, rely=0.9,
                                                                                      width='120', height='60')

            # button calls end_test function
            Button(self, text='End Test', bg='#ff4d4d', fg='black', font='Arial 16 bold',
                   command=lambda: controller.show_frame("ConfirmationPage")).place(anchor='w', relx=0.225, rely=0.9, width='120', height='60')

        # button calls start_test function
        Button(self, text='Start Test', bg='#47d147', fg='black', font='Arial 16 bold',
               command=start_test).place(anchor='w', relx=0.03, rely=0.125, width='120', height='80')


if __name__ == "__main__":
    app = Application()
    app.mainloop()
