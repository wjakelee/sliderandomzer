from tkinter import *

class Login(Frame):  # Sample Login page

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        Label(self, text="Please enter the following information:", font='Arial 22 bold').place(relx=0.5, rely=0.2,
                                                                                                anchor='n')

        username = StringVar()
        password = StringVar()

        Label(self, text="Username:", font='Arial 16 bold').place(relx=0.5, rely=0.35, anchor='n')
        Entry(self, textvariable=username).place(relx=0.5, rely=0.4, anchor='n')  # username entry

        Label(self, text="Password:", font='Arial 16 bold').place(relx=0.5, rely=0.55, anchor='n')
        Entry(self, show="*", textvariable=password).place(relx=0.5, rely=0.6, anchor='n')  # password entry

        # button commands check_entry function
        Button(self, text="Enter", font='Arial 16 bold', fg="black", bg="grey", height='3', width='10',
               command=lambda: check_entry(username.get(), password.get())).place(relx=0.5, rely=0.7, anchor='n')

        # button calls show_frame method and takes you page to Start Page
        Button(self, text="Back To Home", fg="black", bg="#81DAF5", font="Arial 14", width='15', height='2',
               command=lambda: controller.show_frame("StartPage")).place(relx=1.0, rely=1.0, anchor=SE)

        # Function checks to see if the entered username/password are correct and calls show_frame module to raise
        # the SetDatRand frame
        def check_entry(username, password):
            if username == "admin" and password == "password":
                # reset username and password variable ""
                controller.show_frame("SetDatRand")                   # raises SetDatRand frame

# need to figure how to run this module on its own

if __name__ == "__main__":
    app = Tk()
    app.mainloop()