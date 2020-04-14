from tkinter import *
import os
from tkinter import filedialog
from tkinter import messagebox
import csv
import random
from collections import MutableMapping


# choose to randomize order or export data page
class RandAndFile(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

        # generates a list of random numbers from 1-60 w/o repeats
        def generate_random():
            with open('temporary_file.csv', 'r', newline="") as temp_file:      # open file for reading
                reader = csv.reader(temp_file)
                import_list = []
                for row in reader:
                    import_list.append(row)         # creates list of case order

            random.shuffle(import_list)         # shuffles randomization order

            with open('temp_file_change.csv', 'w', newline="") as change_file:      # open file for writing
                writer = csv.writer(change_file)
                for row in import_list:
                    writer.writerow(row)            # writes each row into file

            os.remove('temporary_file.csv')
            os.rename('temp_file_change.csv', 'temporary_file.csv')     # renames file

            # checks if randomization list was generated or not, prompts user
            if import_list == []:
                messagebox.showerror(title="No Order Selected!", message="Please set up the test prior to "
                                                                         "selecting a randomization order.")
            else:
                messagebox.showinfo(title="Order Selected", message="Randomization order has been selected and "
                                                                    "re-randomized from the test setup file "
                                                                    "(case_information.csv).")

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

            # checks if randomization list was generated or not, prompts user
            if import_list == []:
                messagebox.showerror(title="No Order Selected!", message="Please set up the test prior to "
                                                                         "selecting a randomization order.")
            else:
                messagebox.showinfo(title="Order Selected", message="Randomization order has been selected from"
                                                                    " the test setup file (case_information.csv).")

        # export file with answers and barcodes
        def export():

            answers = {}
            # pulls answers from the LAST test taken
            with open('previous_ans.csv', 'r', newline='') as prev_ans_file:  # opens selected file for reading
                reader = csv.reader(prev_ans_file)
                next(reader)
                # saves previous test answers to dictionary
                for row in reader:
                    answers[row[0]] = {'Q1': row[1], 'Q2': row[2], 'Q3': row[3], 'Q4': row[4], 'Q5': row[5],
                                       'Q6': row[6], 'Comments':  row[7]}

            barcode_info = {}
            # pulls barcode info from LAST test taken
            with open('temporary_file.csv', 'r', newline='') as temp_file:  # opens selected file for reading
                temp_file_reader = csv.reader(temp_file)
                # saves barcode info from last test to dictionary
                for row in temp_file_reader:
                    barcode_info[row[0]] = {'he': row[1], 'nrc': row[2], 'ab': row[3]}

            # merges barcode_info dictionary with answers dictionary
            def rec_merge(d1, d2):
                # Update two dicts of dicts recursively, if either mapping has leaves that are non-dicts,
                # the second's leaf overwrites the first's.
                for k, v in d1.items():  # in Python 2, use .iteritems()!
                    if k in d2:
                        # this next check is the only difference!
                        if all(isinstance(e, MutableMapping) for e in (v, d2[k])):
                            d2[k] = rec_merge(v, d2[k])
                d3 = d1.copy()
                d3.update(d2)
                return d3

            # final dictionary with all necessary information from previous test
            final_dictionary = dict(rec_merge(answers, barcode_info))

            # updates one dictionary
            def merge_dict(a, b):
                a.update(b)
                return a

            # opens file selector window to choose where to save export file
            selected_file = filedialog.asksaveasfilename(title="Choose where to dave your file.",
                                                         filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))

            # fields for final export file
            fields = ['Case', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Comments', 'he', 'nrc', 'ab']
            with open(selected_file, 'w', newline='') as export_file:  # opens selected file for reading
                writer = csv.DictWriter(export_file, fields)
                writer.writeheader()
                for case, values in final_dictionary.items():
                    writer.writerow(merge_dict({'Case': case}, values))

            # function adds name date and time to top of export file
            def prepend_line(file_name, line):
                # define name of temporary dummy file
                dummy_file = file_name + '.bak'
                # open original file in read mode and dummy file in write mode
                with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
                    # Write given line to the dummy file
                    write_obj.write(line + '\n')
                    # Read lines from original file one by one and append them to the dummy file
                    for line in read_obj:
                        write_obj.write(line)
                # remove original file
                os.remove(file_name)
                # Rename dummy file as the original file
                os.rename(dummy_file, file_name)

            # pulls user name/date information from last test
            with open('name_date.txt', 'r', newline='') as name_file:  # opens selected file for reading
                name_date_time = name_file.read()

            # adds name and date to top of file
            prepend_line(selected_file, name_date_time)

        # button calls import_random function
        Button(self, text="Import Randomization Order", fg="black", font='Arial 14 bold', width='30',
               height='3', bg="#cc99ff", command=import_random).place(relx=0.5, rely=0.2, anchor=CENTER)

        # button calls generate_random function
        Button(self, text="Generate Randomization Order", font='Arial 14 bold', width='30', height='3',
               fg="black", bg="#ffcc66", command=generate_random).place(relx=0.5, rely=0.45, anchor=CENTER)

        # button calls export function
        Button(self, text="Export Data", font='Arial 14 bold', width='30', height='3',
               fg="black", bg="#99ff66", command=export).place(relx=0.5, rely=0.7, anchor=CENTER)

        # button calls show_frame method and takes you page to Start Page
        Button(self, text="Back To Home", fg="black", bg="#81DAF5", font="Arial 14", width='12', height='1',
               command=lambda: controller.show_frame("StartPage")).place(relx=1.0, rely=1.0, anchor=SE)

        # button calls show_frame method and takes you back one page to SetDatRand
        Button(self, text="Back", fg="black", bg="#81DAF5", font="Arial 14", width='12', height='1',
               command=lambda: controller.show_frame("SetDatRand")).place(relx=0.8, rely=1.0, anchor=SE)
