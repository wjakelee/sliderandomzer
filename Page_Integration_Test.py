from tkinter import *
from Test_Setup import TestSetup
from Set_Dat_Rand import SetDatRand
from Login_Page import Login
from Start_Page import StartPage
from Rand_And_Data import RandAndFile
from Test_Intro_Page import TestIntro
from Questionnaire_Page import QuestionPage


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

        for name, F in self.pages.items():                      # loops through dictionary 'pages'
            frame = F(container, self)                              # assigns iterated frame to a variable 'frame'
            frame.grid(row=0, column=0, sticky="nsew")              # frame positioning
            self.frames[name] = frame                               # adds each page frame to dictionary of frames

        self.show_frame("StartPage")              # calls show_frame method to raise StartPage frame when run

    def show_frame(self, page):
        frame = self.frames[page]               # selects frame to be raised, determined by button click
        frame.tkraise()                         # raises frame called


app = Application()
app.mainloop()
