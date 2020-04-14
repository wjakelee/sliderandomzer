from tkinter import *
from tkinter import messagebox
import datetime
import csv


class TestIntro(Frame):                         # start up / home page, class inherits Frame

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # instructional label
        Label(self, text="Please Enter Your Name:",
              font='Arial 20 bold').place(relx=0.5, rely=0.15, anchor='n')

        # name label
        Label(self, text="(first and last)", fg="black",
              font='Arial 12').place(relx=0.7, rely=0.4, anchor=CENTER)

        name = StringVar()

        # entry for users name
        Entry(self, background='#BDBDBD', textvariable=name, font="Arial 18").place(relx=0.5, rely=0.4, anchor=CENTER, width='200', height='50')

        # Button saves users entries
        Button(self, text="Save", fg="black", bg="#80bfff", font="Arial 14", width='20',
               height='2', command=lambda: user_info(name)).place(relx=.5, rely=.625, anchor=CENTER)

        # button calls show_frame method and takes you page to Start Page
        Button(self, text="Back To Home", fg="black", bg="#81DAF5", font="Arial 14", width='15', height='1',
               command=lambda: controller.show_frame("StartPage")).place(relx=1.0, rely=1.0, anchor=SE)

        # notifies user that test has already been taken
        def next_page():
            name.set("")
            # label covers functionality of page if the test has already been taken
            Label(self, text='You have already taken this test.', fg="black", bg="white", font="Arial 14", width='200',
                  height='20', ).place(relx=0.5, rely=0, anchor='n')
            controller.show_frame("QuestionPage")

        # function writes user information to export file
        def user_info(name):
            x = datetime.datetime.now()             # records date and time when "save" is pressed
            info_list = [name.get(), x]
            with open('name_date.txt', 'w') as export_file:       # opens a temporary file used later
                export_file_writer = csv.writer(export_file)        # creates a csv writer
                export_file_writer.writerow(info_list)

            # checks if user entered their name or not
            if name.get() == "":
                messagebox.showerror(title="Enter Name", message="Please enter your name.")

            if name.get() != "":
                # Button takes user them to the questionnaire page
                Button(self, text="Begin The Test", fg="black", bg="#47d147", font="Arial 14", width='20',
                       height='2', command=next_page).place(relx=.5, rely=.8, anchor=CENTER)
