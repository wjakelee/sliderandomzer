from tkinter import *


class SetDatRand(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # prompt label for user
        Label(self, text="Select an option below:", font='Arial 20 bold').place(relx=0.5, rely=0.1, anchor='n')

        # button calls show_frame method and takes you to TestSetup page
        Button(self, text="Test Setup", fg="black", font='Arial 14 bold', width='25', height='3',
               bg="#47d147", command=lambda: controller.show_frame("TestSetup")).place(relx=0.5, rely=0.35, anchor=CENTER)

        # button takes you to Data File and Randomization page
        Button(self, text="Data File & Randomization", font='Arial 14 bold', width='25', height='3', fg="black",
               bg="#80bfff", command=lambda: controller.show_frame("RandAndFile")).place(relx=0.5, rely=0.6, anchor=CENTER)

        # button calls show_frame method and takes you to Start Page
        Button(self, text="Back To Home", fg="black", bg="#81DAF5", font="Arial 14", width='12', height='1',
               command=lambda: controller.show_frame("StartPage")).place(relx=1.0, rely=1.0, anchor=SE)
