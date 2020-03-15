from tkinter import *


class TestIntro(Frame):                         # start up / home page, class inherits Frame

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # instructional label
        Label(self, text="Please Enter The Following Information:", font='Arial 20 bold',
              bg="white").place(relx=0.5, rely=0.1, anchor='n')

        # name label
        Label(self, text="Name:", fg="black", background='white',
              font='Arial 14 bold').place(relx=0.38, rely=0.25, anchor=CENTER)

        # date label
        Label(self, text="Date:", fg="black", background='white',
              font='Arial 14 bold').place(relx=0.38, rely=0.35, anchor=CENTER)

        # time label
        Label(self, text="Time:", fg="black", background='white',
              font='Arial 14 bold').place(relx=0.38, rely=0.45, anchor=CENTER)

        # Button saves users entries and take them to the questionnaire page
        Button(self, text="Submit To Being The Test", fg="black",
               bg="#9FF781", font="Arial 14", width='25', height='2').place(relx=.5, rely=.6, anchor=CENTER)

        # entry for users name
        Entry(self, background='light gray').place(relx=0.55, rely=0.25, anchor=CENTER)

        # entry for the date
        Entry(self, background='light gray').place(relx=0.55, rely=0.35, anchor=CENTER)

        # entry for the time
        Entry(self, background='light gray').place(relx=0.55, rely=0.45, anchor=CENTER)

        # button calls show_frame method and takes you page to Start Page
        Button(self, text="Back To Home", fg="black", bg="#81DAF5", font="Arial 14", width='15', height='2',
               command=lambda: controller.show_frame("StartPage")).place(relx=1.0, rely=1.0, anchor=SE)

# need to figure how to run this module on its own


if __name__ == "__main__":
    app = Tk()
    app.mainloop()
