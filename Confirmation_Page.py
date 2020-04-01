from tkinter import *
# from IOPi import IOPi # (COMMENT  WHEN TESTING WITHOUT HARDWARE)


class ConfirmationPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        def end_test():
            # initializing port directions for LED illumination (COMMENT LINES 11-25 WHEN TESTING WITHOUT HARDWARE)
            # bus1 = IOPi(0x20)
            # bus1.set_port_direction(0, 0x00)                 # set port direction
            # bus1.write_port(0, 0x00)                         # write port
            #
            # bus2 = IOPi(0x21)
            # bus2.set_port_direction(0, 0x00)                 # set port direction
            # bus2.write_port(0, 0x00)                         # write port
            #
            # bus3 = IOPi(0x22)
            # bus3.set_port_direction(0, 0x00)                 # set port direction
            # bus3.write_port(0, 0x00)                         # write port
            #
            # bus4 = IOPi(0x23)
            # bus4.set_port_direction(0, 0x00)                 # set port direction
            # bus4.write_port(0, 0x00)                         # write port
            #
            # # makes sure ALL LEDs are OFF when test ends (COMMENT WHEN TESTING WITHOUT HARDWARE)
            # for i in range(1, 17):
            #     bus1.write_pin(i, 0)
            #     bus2.write_pin(i, 0)
            #     bus3.write_pin(i, 0)
            #     bus4.write_pin(i, 0)

            # show next page
            controller.show_frame("TestCompletePage")

        Label(self, text="Are You Sure You Want To End The Test?", font='Arial 20 bold',).place(relx=0.5,
                                                                                                rely=0.1, anchor='n')

        Button(self, text="Yes.\nI am finished.", fg="black", font="Arial 14 bold", width="25", height="3",
               bg="#47d147", command=end_test).place(relx=.5, rely=.4, anchor=CENTER)

        Button(self, text="No.\nReturn to test.", fg="black", font="Arial 14 bold", width="25", height="3",
               bg="#ff4d4d", command=lambda: controller.show_frame("QuestionPage")).place(relx=.5, rely=.7,
                                                                                          anchor=CENTER)
