from tkinter import *
from tkinter import messagebox
import datetime
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
        Label(self, text="Please Enter Your Name:",
              font='Arial 20 bold').place(relx=0.5, rely=0.15, anchor='n')

        # name label
        Label(self, text="(first and last)", fg="black",
              font='Arial 12').place(relx=0.7, rely=0.35, anchor=CENTER)

        name = StringVar()

        # entry for users name
        Entry(self, background='light gray', textvariable=name, font="Arial 12").place(relx=0.5, rely=0.35, anchor=CENTER, width='190', height='30')

        # Button saves users entries
        Button(self, text="Save", fg="black", bg="#80bfff", font="Arial 14", width='20',
               height='2', command=lambda: user_info(name)).place(relx=.5, rely=.55, anchor=CENTER)

        # button calls show_frame method and takes you page to Start Page
        Button(self, text="Back To Home", fg="black", bg="#81DAF5", font="Arial 14", width='15', height='1',
               command=lambda: controller.show_frame("StartPage")).place(relx=1.0, rely=1.0, anchor=SE)

        def next_page():
            name.set("")
            Label(self, text='You have already taken this test.', fg="black", bg="white", font="Arial 14", width='200',
                  height='20', ).place(relx=0.5, rely=0, anchor='n')
            controller.show_frame("QuestionPage")

        # function writes user information to export file
        def user_info(name):
            x = datetime.datetime.now()             # records date and time when "save" is pressed
            info_list = [name.get(), x]
            with open('export_file.csv', 'w') as export_file:       # opens a temporary file used later
                export_file_writer = csv.writer(export_file)        # creates a csv writer
                export_file_writer.writerow(info_list)

            if name.get() == "":
                messagebox.showerror(title="Enter Name", message="Please enter your name.")

            if name.get() != "":
                # Button takes user them to the questionnaire page
                Button(self, text="Begin The Test", fg="black", bg="#47d147", font="Arial 14", width='20',
                       height='2', command=next_page).place(relx=.5, rely=.8, anchor=CENTER)


if __name__ == "__main__":
    app = Application()
    app.mainloop()

