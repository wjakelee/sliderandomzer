from tkinter import *


class TestCompletePage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # label to confirm test complete
        Label(self, text="Test Complete.", font='Arial 20 bold').place(relx=0.5, rely=0.1, anchor='n')

        # back to home button
        Button(self, text="Back To Home", fg="black", font="Arial 14 bold", width="25", height="3",
               bg="#01DF3A", command=lambda: controller.show_frame("StartPage")).place(relx=.5, rely=.4, anchor=CENTER)
