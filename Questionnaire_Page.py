from tkinter import *
import csv
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

        # need to finish start_test function, reads randomization order for temporary_file.csv and begins test
        def start_test():

            with open('temporary_file.csv', 'r', newline="") as temp_file:          # open temporary file
                reader = csv.reader(temp_file)
                order_list = []
                for row in reader:
                    order_list.append(row[0])                # determine order of cases from first column of temp file

            test_answers = {}

            def save_answers(test_answers, case, ans_1, ans_2, ans_3, ans_4, ans_5, ans_6, comments):
                test_answers[case] = {'Q1': ans_1, 'Q2': ans_2, 'Q3': ans_3, 'Q4': ans_4,
                                      'Q5': ans_5, 'Q6': ans_6, 'Comments':  comments}
                print(test_answers)

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

            Label(self, text='Case #', background='light gray',
                  font='Arial 18').place(anchor='w', relx=.03, rely=.3, width='100', height='50')

            number = StringVar()  # makes number variable type String
            number.set(order_list[0])  # sets number variable to first number in order list
            Label(self, textvariable=number, font='Arial 18',
                  background='light gray').place(anchor='w', relx=.15, rely=.3, width='35', height='50')

            Label(self, text='1. Evaluate all slides in case.\n2. Answer all questions.'
                             '\n3. Save Answers.\n4. Press "next case" for\nnew case evaluation.',
                  background='light gray', font='Arial 10', justify=LEFT).place(anchor='w', relx=.03, rely=.5,
                                                                                width='200', height='120')


            # NEED TO FIGURE OUT HOW TO STEP TO NEXT CASE IN ORDER_LIST
            # def next_case(order_list):
            #     # CASE NUMBER OUTPUT
            #     next(order_list)
            #     Label(self, text='Case #', background='light gray',
            #           font='Arial 18').place(anchor='w', relx=.03, rely=.3, width='100', height='50')
            #
            #     number = StringVar()            # makes number variable type String
            #     number.set(order_list)            # sets number variable to first number in order list
            #     Label(self, textvariable=number, font='Arial 18',
            #           background='light gray').place(anchor='w', relx=.15, rely=.3, width='35', height='50')
            #
            #     Label(self, text='1. Evaluate all slides in case.\n2. Answer all questions.'
            #                      '\n3. Save Answers.\n4. Press "next case" for\nnew case evaluation.',
            #           background='light gray', font='Arial 10', justify=LEFT).place(anchor='w', relx=.03, rely=.5,
            #                                                                         width='200', height='120')
            #
            #     # button calls save_answers function
            #     Button(self, text='Save Answers', bg='#33adff', fg='black', font='Arial 16 bold',
            #            command=lambda: save_answers(test_answers, order_list[0], ans_1.get(), ans_2.get(), ans_3.get(),
            #                                         ans_4.get(), ans_5.get(), ans_6.get(),
            #                                         comments.get())).place(anchor='w', relx=0.725, rely=0.9,
            #                                                                width='160', height='40')

            # button calls next_case function
            # Button(self, text='Next Case', bg='#bfbfbf', fg='black',
            #       font='Arial 16 bold', command=lambda: next_case(order_list)).place(anchor='w', relx=0.03, rely=0.9, width='120', height='60')

            # button calls end_test function, still need to add this function
            Button(self, text='End Test', bg='#ff4d4d', fg='black',
                   font='Arial 16 bold').place(anchor='w', relx=0.225, rely=0.9, width='120', height='60')

        # button calls start_test function
        Button(self, text='Start Test', bg='#47d147', fg='black', font='Arial 16 bold',
               command=start_test).place(anchor='w', relx=0.03, rely=0.125, width='120', height='80')


if __name__ == "__main__":
    app = Application()
    app.mainloop()
