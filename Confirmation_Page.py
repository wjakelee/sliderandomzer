from tkinter import *


class ConfirmationPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        Label(self, text="Are You Sure You Want To End The Test?", font='Arial 20 bold',).place(relx=0.5,
                                                                                                rely=0.1, anchor='n')

        Button(self, text="Yes.\nI am finished.", fg="black", font="Arial 14 bold", width="25", height="3",
               bg="#01DF3A", command=lambda: controller.show_frame("TestCompletePage")).place(relx=.5, rely=.4,
                                                                                              anchor=CENTER)

        Button(self, text="No.\nReturn to test.", fg="black", font="Arial 14 bold", width="25", height="3",
               bg="#FF0000", command=lambda: controller.show_frame("QuestionPage")).place(relx=.5, rely=.7,
                                                                                          anchor=CENTER)
