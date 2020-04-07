from tkinter import *
from tkinter import messagebox
from Test_Setup import TestSetup
from Set_Dat_Rand import SetDatRand
from Start_Page import StartPage
from Rand_And_Data import RandAndFile
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
        self.pages = {'StartPage': StartPage, 'Login': Login, 'SetDatRand': SetDatRand, 'TestSetup': TestSetup,
                      'RandAndFile': RandAndFile, 'TestIntro': TestIntro, 'QuestionPage': QuestionPage}

        # loop creates a frame for each page
        for name, F in self.pages.items():                      # loops through dictionary 'pages'
            frame = F(container, self)                              # assigns iterated frame to a variable 'frame'
            frame.grid(row=0, column=0, sticky="nsew")              # frame positioning
            self.frames[name] = frame                               # adds each page frame to dictionary of frames

        self.show_frame("Login")              # calls show_frame method to raise StartPage frame when run

    def show_frame(self, page):
        frame = self.frames[page]               # selects frame to be raised, determined by button click
        frame.tkraise()                         # raises frame called


class Login(Frame):  # Sample Login page

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        Label(self, text="Please enter a PIN:", font='Arial 22 bold').place(relx=0.5, rely=0.15, anchor='n')

        number = StringVar()

        Entry(self, textvariable=number, background='#BDBDBD',
              font='Arial 18').place(relx=0.5, rely=0.375, anchor='n', height='50', width='200',)  # username entry

        # button commands check_entry function
        Button(self, text="Enter", font='Arial 16 bold', fg="black", bg="#80bfff", height='2', width='15',
               command=lambda: check_entry(number)).place(relx=0.5, rely=0.65, anchor='n')

        # button calls show_frame method and takes you page to Start Page
        Button(self, text="Back To Home", fg="black", bg="#81DAF5", font="Arial 14", width='12', height='1',
               command=lambda: controller.show_frame("StartPage")).place(relx=1.0, rely=1.0, anchor=SE)

        # Function checks to see if the entered username/password are correct and calls show_frame module to raise
        # the SetDatRand frame
        def check_entry(number):
            if number.get() == "1234":
                number.set("")
                controller.show_frame("SetDatRand")                   # raises SetDatRand frame
            else:
                messagebox.showerror(title="Invalid", message="Incorrect PIN.")


if __name__ == "__main__":
    app = Application()
    app.mainloop()
