from tkinter import *
from tkinter import messagebox
import csv
from Start_Page import StartPage

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
        self.pages = {'StartPage': StartPage, 'TestIntro': TestIntro}

        # loop creates a frame for each page
        for name, F in self.pages.items():                      # loops through dictionary 'pages'
            frame = F(container, self)                              # assigns iterated frame to a variable 'frame'
            frame.grid(row=0, column=0, sticky="nsew")              # frame positioning
            self.frames[name] = frame                               # adds each page frame to dictionary of frames

        self.show_frame("TestIntro")              # calls show_frame method to raise StartPage frame when run

    def show_frame(self, page):
        frame = self.frames[page]               # selects frame to be raised, determined by button click
        frame.tkraise()                         # raises frame called


class TestIntro(Frame):                         # start up / home page, class inherits Frame

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # instructional label
        Label(self, text="Please Enter The Following Information:",
              font='Arial 20 bold').place(relx=0.5, rely=0.1, anchor='n')

        # name label
        Label(self, text="Name:", fg="black",
              font='Arial 14 bold').place(relx=0.3, rely=0.25, anchor='w')

        # date label
        Label(self, text="Date:", fg="black",
              font='Arial 14 bold').place(relx=0.3, rely=0.35, anchor='w')

        # time label
        Label(self, text="Time:", fg="black",
              font='Arial 14 bold').place(relx=0.3, rely=0.45, anchor='w')

        # name label
        Label(self, text="(first and last)", fg="black",
              font='Arial 10').place(relx=0.65, rely=0.25, anchor='w')

        # date label
        Label(self, text="(xx/xx/xxx)", fg="black",
              font='Arial 10').place(relx=0.65, rely=0.35, anchor='w')

        # time label
        Label(self, text="(xx:xx AM/PM)", fg="black",
              font='Arial 10').place(relx=0.65, rely=0.45, anchor='w')

        name = StringVar()
        date = StringVar()
        time = StringVar()

        # entry for users name
        Entry(self, background='light gray', textvariable=name).place(relx=0.4, rely=0.25, anchor='w', width='190')

        # entry for the date
        Entry(self, background='light gray', textvariable=date).place(relx=0.4, rely=0.35, anchor='w', width='190')

        # entry for the time
        Entry(self, background='light gray', textvariable=time).place(relx=0.4, rely=0.45, anchor='w', width='190')

        # Button saves users entries
        Button(self, text="Save Information", fg="black", bg="#80bfff", font="Arial 14", width='20',
               height='2', command=lambda: user_info(name.get(), date.get(), time.get())).place(relx=.5, rely=.6, anchor=CENTER)

        # button calls show_frame method and takes you page to Start Page
        Button(self, text="Back To Home", fg="black", bg="#81DAF5", font="Arial 14", width='15', height='1',
               command=lambda: controller.show_frame("StartPage")).place(relx=1.0, rely=1.0, anchor=SE)

        # function writes user information to export file
        def user_info(name, date, time):
            info_list = [name, date, time]
            with open('export_file.csv', 'w') as export_file:       # opens a temporary file used later
                export_file_writer = csv.writer(export_file)        # creates a csv writer
                export_file_writer.writerow(info_list)

            if name == "" or date == "" or time == "":
                messagebox.showerror(title="Missing Fields", message="Entry fields are missing data.")

            if name != "" and date != "" and time != "":
                # Button takes user them to the questionnaire page
                Button(self, text="Begin The Test", fg="black", bg="#47d147", font="Arial 14", width='20',
                       height='2', command=lambda: controller.show_frame("QuestionPage")).place(relx=.5, rely=.8,
                                                                                                anchor=CENTER)


if __name__ == "__main__":
    app = Application()
    app.mainloop()

