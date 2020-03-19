from tkinter import *
from tkinter import messagebox

class Login(Frame):  # Sample Login page

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        Label(self, text="Please enter the following information:", font='Arial 22 bold').place(relx=0.5, rely=0.15,
                                                                                                anchor='n')

        username = StringVar()
        password = StringVar()

        Label(self, text="Username:", font='Arial 16 bold').place(relx=0.5, rely=0.3, anchor='n')
        Entry(self, textvariable=username, background='light grey',
              font='Arial 14').place(relx=0.5, rely=0.375, anchor='n', width='180',)  # username entry

        Label(self, text="Password:", font='Arial 16 bold').place(relx=0.5, rely=0.5, anchor='n')
        Entry(self, show="*", textvariable=password, background='light grey',
              font='Arial 14').place(relx=0.5, rely=0.575, anchor='n', width='180',)  # password entry

        # button commands check_entry function
        Button(self, text="Enter", font='Arial 16 bold', fg="black", bg="#33adff", height='2', width='10',
               command=lambda: check_entry(username, password)).place(relx=0.5, rely=0.7, anchor='n')

        # button calls show_frame method and takes you page to Start Page
        Button(self, text="Back To Home", fg="black", bg="#81DAF5", font="Arial 14", width='15', height='1',
               command=lambda: controller.show_frame("StartPage")).place(relx=1.0, rely=1.0, anchor=SE)

        # Function checks to see if the entered username/password are correct and calls show_frame module to raise
        # the SetDatRand frame
        def check_entry(username, password):
            if username.get() == "admin" and password.get() == "password":
                username.set("")
                password.set("")
                controller.show_frame("SetDatRand")                   # raises SetDatRand frame
            else:
                messagebox.showerror(title="Invalid", message="Incorrect username or password.")


# need to figure how to run this module on its own

if __name__ == "__main__":
    app = Tk()
    app.mainloop()