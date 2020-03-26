from tkinter import *
from Confirmation_Page import ConfirmationPage


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
        self.pages = {'TestComplete': TestCompletePage, 'ConfirmationPage': ConfirmationPage}

        # loop creates a frame for each page
        for name, F in self.pages.items():                      # loops through dictionary 'pages'
            frame = F(container, self)                              # assigns iterated frame to a variable 'frame'
            frame.grid(row=0, column=0, sticky="nsew")              # frame positioning
            self.frames[name] = frame                               # adds each page frame to dictionary of frames

        self.show_frame("QuestionPage")              # calls show_frame method to raise StartPage frame when run

    def show_frame(self, page):
        frame = self.frames[page]               # selects frame to be raised, determined by button click
        frame.tkraise()                         # raises frame called


class TestCompletePage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        Label(self, text="Test Complete.", font='Arial 20 bold', bg="white").place(relx=0.5, rely=0.1, anchor='n')

        Button(self, text="Back To Home", fg="black", font="Arial 14 bold", width="25", height="3",
               bg="#01DF3A", command=lambda: controller.show_frame("StartPage")).place(relx=.5, rely=.4, anchor=CENTER)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
