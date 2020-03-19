from tkinter import *


class StartPage(Frame):                         # start up / home page, class inherits Frame

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        Label(self, text="Please select an option below:", font='Arial 22 bold').place(relx=0.5, rely=0.2,
                                                                                                   anchor='n')

        # Button takes you to take test intro page
        Button(self, text="Take Test", fg="black", font='Arial 14 bold', width='15', height='4',
               bg="#47d147", command=lambda: controller.show_frame("TestIntro")).place(relx=0.275, rely=0.5, anchor=CENTER)

        # button calls show_frame method and raises to Login frame
        Button(self, text="Setup, DataFile,\nRandomization (Admin Only)", font='Arial 14 bold', width='25',
               height='4', fg="black", bg="#80bfff", command=lambda: controller.show_frame("Login")).place(
            relx=0.65, rely=0.5, anchor=CENTER)

        # Button exits desktop
        Button(self, text="Exit to Desktop", font="Arial 14", fg="black", bg="#ff4d4d", width='12',
               height='1', command=parent.master.destroy).place(relx=1.0, rely=1.0, anchor=SE)


# need to figure how to run this module on its own

if __name__ == "__main__":
    app = Tk()
    app.mainloop()