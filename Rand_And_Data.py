from tkinter import *
from tkinter import messagebox
import csv
import random


class RandAndFile(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # generates a list of random numbers from 1-60 w/o repeats
        def generate_random():
            with open('temporary_file.csv', 'r') as temp_file:
                reader = csv.reader(temp_file)
                import_list = []
                for row in reader:
                    import_list.append(row[0])
            random.shuffle(import_list)

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
            with open('temporary_file.csv', 'r') as temp_file:
                reader = csv.reader(temp_file)
                import_list = []
                for row in reader:
                    import_list.append(row[0])

            if import_list == []:
                messagebox.showerror(title="No Order Selected!", message="Please set up the test prior to "
                                                                         "selecting a randomization order.")
            else:
                messagebox.showinfo(title="Order Selected", message="Randomization order has been selected from"
                                                                    " the test setup file (case_information.csv).")
            # print(import_list)

        Button(self, text="Import Randomization Order", fg="black", font='Arial 14 bold', width='30',
               height='3', bg="#cc99ff", command=import_random).place(relx=0.5, rely=0.2, anchor=CENTER)

        Button(self, text="Generate Randomization Order", font='Arial 14 bold', width='30', height='3',
               fg="black", bg="#ffcc66", command=generate_random).place(relx=0.5, rely=0.45, anchor=CENTER)

        Button(self, text="Export Data", font='Arial 14 bold', width='30', height='3',
               fg="black", bg="#99ff66").place(relx=0.5, rely=0.7, anchor=CENTER)

        # button calls show_frame method and takes you page to Start Page
        Button(self, text="Back To Home", fg="black", bg="#81DAF5", font="Arial 14", width='12', height='1',
               command=lambda: controller.show_frame("StartPage")).place(relx=1.0, rely=1.0, anchor=SE)

        # button calls show_frame method and takes you back one page to SetDatRand
        Button(self, text="Back", fg="black", bg="#81DAF5", font="Arial 14", width='12', height='1',
               command=lambda: controller.show_frame("SetDatRand")).place(relx=0.8, rely=1.0, anchor=SE)


# need to figure how to run this module on its own

if __name__ == "__main__":
    app = Tk()
    app.mainloop()
