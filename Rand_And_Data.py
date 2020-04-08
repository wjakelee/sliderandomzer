from tkinter import *
import os
from tkinter import filedialog
from tkinter import messagebox
import csv
import random
from collections import MutableMapping
from Test_Setup import TestSetup
from Start_Page import StartPage
from Test_Intro_Page import TestIntro
from Questionnaire_Page import QuestionPage


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
        self.pages = {'StartPage': StartPage, 'TestSetup': TestSetup,
                      'RandAndFile': RandAndFile, 'TestIntro': TestIntro, 'QuestionPage': QuestionPage}

        # loop creates a frame for each page
        for name, F in self.pages.items():                      # loops through dictionary 'pages'
            frame = F(container, self)                              # assigns iterated frame to a variable 'frame'
            frame.grid(row=0, column=0, sticky="nsew")              # frame positioning
            self.frames[name] = frame                               # adds each page frame to dictionary of frames

        self.show_frame("RandAndFile")              # calls show_frame method to raise StartPage frame when run

    def show_frame(self, page):
        frame = self.frames[page]               # selects frame to be raised, determined by button click
        frame.tkraise()                         # raises frame called

class YamlReaderError(Exception):
    pass

class RandAndFile(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

        # generates a list of random numbers from 1-60 w/o repeats
        def generate_random():
            with open('temporary_file.csv', 'r', newline="") as temp_file:
                reader = csv.reader(temp_file)
                import_list = []
                for row in reader:
                    import_list.append(row)

            random.shuffle(import_list)

            with open('temp_file_change.csv', 'w', newline="") as change_file:
                writer = csv.writer(change_file)
                for row in import_list:
                    writer.writerow(row)

            os.remove('temporary_file.csv')
            os.rename('temp_file_change.csv', 'temporary_file.csv')

            if import_list == []:
                messagebox.showerror(title="No Order Selected!", message="Please set up the test prior to "
                                                                         "selecting a randomization order.")
            else:
                messagebox.showinfo(title="Order Selected", message="Randomization order has been selected and "
                                                                    "re-randomized from the test setup file "
                                                                    "(case_information.csv).")
            # print(import_list)

        # imports order of numbers from temporary csv file
        def import_random():
            # opens file selector window
            selected_file = filedialog.askopenfilename(title="Select the setup CSV File",
                                                       filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))

            with open(selected_file, 'r', newline="") as order_file:         # opens selected file for reading
                reader = csv.reader(order_file)                         # reads selected file
                next(reader)
                import_list = []
                for row in reader:
                    import_list.append(row)

            with open(selected_file, 'r', newline="") as order_file:        # opens selected file for reading
                reader = csv.reader(order_file)                         # reads selected file
                next(reader)

                with open('temporary_file.csv', 'w', newline='') as temp_file:   # opens a temporary file used later
                    writer = csv.writer(temp_file)                       # creates a csv writer
                    for line in reader:
                        writer.writerow(line)

            if import_list == []:
                messagebox.showerror(title="No Order Selected!", message="Please set up the test prior to "
                                                                         "selecting a randomization order.")
            else:
                messagebox.showinfo(title="Order Selected", message="Randomization order has been selected from"
                                                                    " the test setup file (case_information.csv).")
            # print(import_list)

        def export():

            answers = {}
            # pulls answers from the LAST test taken
            with open('previous_ans.csv', 'r', newline='') as prev_ans_file:  # opens selected file for reading
                reader = csv.reader(prev_ans_file)
                next(reader)
                for row in reader:
                    answers[row[0]] = {'Q1': row[1], 'Q2': row[2], 'Q3': row[3], 'Q4': row[4], 'Q5': row[5],
                                       'Q6': row[6], 'Comments':  row[7]}

            barcode_info = {}
            # pulls barcode info from LAST test taken
            with open('temporary_file.csv', 'r', newline='') as temp_file:  # opens selected file for reading
                temp_file_reader = csv.reader(temp_file)
                for row in temp_file_reader:
                    barcode_info[row[0]] = {'he': row[1], 'nrc': row[2], 'ab': row[3]}

            def rec_merge(d1, d2):
                '''
                Update two dicts of dicts recursively,
                if either mapping has leaves that are non-dicts,
                the second's leaf overwrites the first's.
                '''
                for k, v in d1.items():  # in Python 2, use .iteritems()!
                    if k in d2:
                        # this next check is the only difference!
                        if all(isinstance(e, MutableMapping) for e in (v, d2[k])):
                            d2[k] = rec_merge(v, d2[k])
                        # we could further check types and merge as appropriate here.
                d3 = d1.copy()
                d3.update(d2)
                return d3

            final_dictionary = dict(rec_merge(answers, barcode_info))

            def merge_dict(a, b):
                a.update(b)
                return a

            fields = ['Case', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Comments', 'he', 'nrc', 'ab']
            with open('export_file.csv', 'w', newline='') as export_file:  # opens selected file for reading
                writer = csv.DictWriter(export_file, fields)
                writer.writeheader()
                for case, values in final_dictionary.items():
                    writer.writerow(merge_dict({'Case': case}, values))

        Button(self, text="Import Randomization Order", fg="black", font='Arial 14 bold', width='30',
               height='3', bg="#cc99ff", command=import_random).place(relx=0.5, rely=0.2, anchor=CENTER)

        Button(self, text="Generate Randomization Order", font='Arial 14 bold', width='30', height='3',
               fg="black", bg="#ffcc66", command=generate_random).place(relx=0.5, rely=0.45, anchor=CENTER)

        Button(self, text="Export Data", font='Arial 14 bold', width='30', height='3',
               fg="black", bg="#99ff66", command=export).place(relx=0.5, rely=0.7, anchor=CENTER)

        # button calls show_frame method and takes you page to Start Page
        Button(self, text="Back To Home", fg="black", bg="#81DAF5", font="Arial 14", width='12', height='1',
               command=lambda: controller.show_frame("StartPage")).place(relx=1.0, rely=1.0, anchor=SE)

        # button calls show_frame method and takes you back one page to SetDatRand
        Button(self, text="Back", fg="black", bg="#81DAF5", font="Arial 14", width='12', height='1',
               command=lambda: controller.show_frame("SetDatRand")).place(relx=0.8, rely=1.0, anchor=SE)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
