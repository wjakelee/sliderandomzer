from tkinter import *
import csv


class QuestionPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # label for question 1
        Label(self, text='1. H&E Acceptable?',
              font='Arial 14').place(anchor='w', relx=.4, rely=.1)

        # label for question 2
        Label(self, text='2. Negative Control Acceptable?',
              font='Arial 14').place(anchor='w', relx=.4, rely=.17)

        # label for question 3
        Label(self, text='3. Case Morphology Acceptable?',
              font='Arial 14').place(anchor='w', relx=.4, rely=.24)

        # label for question 4
        Label(self, text='4. Background Acceptable?',
              font='Arial 14').place(anchor='w', relx=.4, rely=.31)

        # label for question 5
        Label(self, text='5. % Cell Staining (Raw Score, 0-100):',
              font='Arial 14').place(anchor='w', relx=.4, rely=.38)

        # label for question 6
        Label(self, text='6. Case Status:',
              font='Arial 14').place(anchor='w', relx=.4, rely=.45)

        # label for comments
        Label(self, text='7. Comments:',
              font='Arial 14').place(anchor='w', relx=.4, rely=.52)

        comments = StringVar()

        # entry field for comments
        Entry(self, textvariable=comments, background='#e6e6e6', font='Arial 12', ).place(
            anchor='w', relx=.4, rely=.68, width='430', height='120')

        # need to finish start_test function, reads randomization order for temporary_file.csv and begins test
        def start_test():
            order = [1, 2, 3]                   # temporary order, I will change this to []

            # need to get this part to read a single column of temporary_file
            # with open('temporary_file.csv', 'r', newline='') as random_order:
            #     file_reader = csv.reader(random_order)

            Label(self, text='Case #', background='light gray',
                  font='Arial 18').place(anchor='w', relx=.03, rely=.3, width='100', height='50')

            number = StringVar()            # makes number variable type String
            number.set(order[0])            # sets number variable to first number in order list
            Label(self, textvariable=number, font='Arial 18',
                  background='light gray').place(anchor='w', relx=.14, rely=.3, width='25', height='50')

        # button calls start_test function
        Button(self, text='Start Test', bg='#47d147', fg='black', font='Arial 16 bold',
               command=start_test).place(anchor='w', relx=0.03, rely=0.125, width='120', height='80')

        # button calls next_case function, still need to add this function
        Button(self, text='Next Case', bg='#bfbfbf', fg='black',
               font='Arial 16 bold').place(anchor='w', relx=0.03, rely=0.9, width='120', height='60')

        # button calls end_test function, still need to add this function
        Button(self, text='End Test', bg='#ff4d4d', fg='black',
               font='Arial 16 bold').place(anchor='w', relx=0.225, rely=0.9, width='120', height='60')

        # button calls save_answers function, still need to add this function
        Button(self, text='Save Answers', bg='#33adff', fg='black',
               font='Arial 16 bold').place(anchor='w', relx=0.725, rely=0.875, width='160', height='40')


# need to figure how to run this module on its own


if __name__ == "__main__":
    app = Tk()
    app.mainloop()
