from tkinter import *
from tkinter import messagebox


class Login(Frame):  # Login page

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # prompt to enter pin
        Label(self, text="Please enter a PIN:", font='Arial 22 bold').place(relx=0.5, rely=0.15, anchor='n')

        number = StringVar()    # initialize number variable type

        # entry field for pin entry
        Entry(self, textvariable=number, background='#BDBDBD', justify=CENTER,
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