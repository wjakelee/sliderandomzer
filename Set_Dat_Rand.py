from tkinter import *
from Test_Setup import TestSetup
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
        self.pages = {'StartPage': StartPage, 'SetDatRand': SetDatRand, 'TestSetup': TestSetup,
                      'RandAndFile': RandAndFile, 'TestIntro': TestIntro, 'QuestionPage': QuestionPage}

        # loop creates a frame for each page
        for name, F in self.pages.items():                      # loops through dictionary 'pages'
            frame = F(container, self)                              # assigns iterated frame to a variable 'frame'
            frame.grid(row=0, column=0, sticky="nsew")              # frame positioning
            self.frames[name] = frame                               # adds each page frame to dictionary of frames

        self.show_frame("SetDatRand")              # calls show_frame method to raise StartPage frame when run

    def show_frame(self, page):
        frame = self.frames[page]               # selects frame to be raised, determined by button click
        frame.tkraise()                         # raises frame called


class SetDatRand(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        Label(self, text="Select an option below:", font='Arial 20 bold').place(relx=0.5, rely=0.1,
                                                                                       anchor='n')

        # button calls show_frame method and takes you to TestSetup page
        Button(self, text="Test Setup", fg="black", font='Arial 14 bold', width='25', height='3',
               bg="#47d147", command=lambda: controller.show_frame("TestSetup")).place(relx=0.5, rely=0.35, anchor=CENTER)

        # button takes you to Data File and Randomization page
        Button(self, text="Data File & Randomization", font='Arial 14 bold', width='25', height='3', fg="black",
               bg="#80bfff", command=lambda: controller.show_frame("RandAndFile")).place(relx=0.5, rely=0.6, anchor=CENTER)

        # button calls show_frame method and takes you to Start Page
        Button(self, text="Back To Home", fg="black", bg="#81DAF5", font="Arial 14", width='12', height='1',
               command=lambda: controller.show_frame("StartPage")).place(relx=1.0, rely=1.0, anchor=SE)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
