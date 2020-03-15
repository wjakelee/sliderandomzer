from tkinter import *
import csv


class TestIntro(Frame):                         # start up / home page, class inherits Frame

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # instructional label
        Label(self, text="Please Enter The Following Information:", font='Arial 20 bold',
              bg="white").place(relx=0.5, rely=0.1, anchor='n')

        # name label
        Label(self, text="Name:", fg="black", background='white',
              font='Arial 14 bold').place(relx=0.37, rely=0.25, anchor=CENTER)

        # date label
        Label(self, text="Date:", fg="black", background='white',
              font='Arial 14 bold').place(relx=0.37, rely=0.35, anchor=CENTER)

        # time label
        Label(self, text="Time:", fg="black", background='white',
              font='Arial 14 bold').place(relx=0.37, rely=0.45, anchor=CENTER)

        # name label
        Label(self, text="(first and last)", fg="black", background='white',
              font='Arial 10').place(relx=0.72, rely=0.25, anchor=CENTER)

        # date label
        Label(self, text="(xx/xx/xxx)", fg="black", background='white',
              font='Arial 10').place(relx=0.71, rely=0.35, anchor=CENTER)

        # time label
        Label(self, text="(xx:xx AM/PM)", fg="black", background='white',
              font='Arial 10').place(relx=0.72, rely=0.45, anchor=CENTER)

        name = StringVar()
        date = StringVar()
        time = StringVar()

        # entry for users name
        Entry(self, background='light gray', textvariable=name).place(relx=0.55, rely=0.25, anchor=CENTER)

        # entry for the date
        Entry(self, background='light gray', textvariable=date).place(relx=0.55, rely=0.35, anchor=CENTER)

        # entry for the time
        Entry(self, background='light gray', textvariable=time).place(relx=0.55, rely=0.45, anchor=CENTER)

        # Button saves users entries
        Button(self, text="Save Information", fg="black", bg="#9FF781", font="Arial 14", width='25',
               height='2', command=lambda: user_info(name.get(), date.get(), time.get())).place(relx=.5, rely=.6, anchor=CENTER)

        # Button takes user them to the questionnaire page
        Button(self, text="Being The Test", fg="black", bg="#9FF781", font="Arial 14", width='25',
               height='2', command=lambda: controller.show_frame("QuestionPage")).place(relx=.5, rely=.73, anchor=CENTER)

        # button calls show_frame method and takes you page to Start Page
        Button(self, text="Back To Home", fg="black", bg="#81DAF5", font="Arial 14", width='15', height='2',
               command=lambda: controller.show_frame("StartPage")).place(relx=1.0, rely=1.0, anchor=SE)

        # function writes user information to export file
        def user_info(name, date, time):
            info_list = [name, date, time]
            with open('export_file.csv', 'w') as export_file:       # opens a temporary file used later
                export_file_writer = csv.writer(export_file)        # creates a csv writer
                export_file_writer.writerow(info_list)

# need to figure how to run this module on its own


if __name__ == "__main__":
    app = Tk()
    app.mainloop()
