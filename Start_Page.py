from tkinter import *


class StartPage(Frame):                         # start up / home page, class inherits Frame

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        Label(self, text="Please select an option below:", font='Arial 22 bold', bg="white").place(relx=0.5, rely=0.2,
                                                                                                   anchor='n')

        # Button takes you to take test page (still need to setup this page)
        Button(self, text="Take Test", fg="black", font='Arial 14 bold', width='20', height='5',
               bg="#33cc33").place(relx=0.3, rely=0.5, anchor=CENTER)

        # button calls show_frame method and raises to Login frame
        Button(self, text="Setup, DataFile,\nRandomization (Admin Only)", font='Arial 14 bold', width='30',
               height='5', fg="black", bg="#6699ff", command=lambda: controller.show_frame("Login")).place(
            relx=0.65, rely=0.5, anchor=CENTER)

        # Button exits desktop (doesnt do anything yet, may not actually need this button)
        Button(self, text="Exit to Desktop", font="Arial 14", fg="black", bg="#ff4d4d", width='15',
               height='2').place(relx=1.0, rely=1.0, anchor=SE)


# need to figure how to run this module on its own

if __name__ == "__main__":
    app = Tk()
    app.mainloop()