from tkinter import *
try:
    from IOPi import IOPi
except ModuleNotFoundError:
    from test import Bus as IOPi


# initializing port directions for LED illumination
bus1 = IOPi(0x20)                                # I2C address (bus 1, board 1)
bus1.set_port_direction(0, 0x00)                 # 0: pins 1-8, 0x00: set port direction as output
bus1.set_port_direction(1, 0x00)                 # 1: pins 9-16, 0x00: set port direction as output
bus1.write_port(0, 0x00)                         # initially turn off all pins

bus2 = IOPi(0x21)                                # I2C address (bus 2, board 1)
bus2.set_port_direction(0, 0x00)                 # 0: pins 1-8, 0x00: set port direction as output
bus2.set_port_direction(1, 0x00)                 # 1: pins 9-16, 0x00: set port direction as output
bus2.write_port(0, 0x00)                         # initially turn off all pins

bus3 = IOPi(0x22)                                # I2C address (bus 1, board 2)
bus3.set_port_direction(0, 0x00)                 # 0: pins 1-8, 0x00: set port direction as output
bus3.set_port_direction(1, 0x00)                 # 1: pins 9-16, 0x00: set port direction as output
bus3.write_port(0, 0x00)                         # initially turn off all pins

bus4 = IOPi(0x23)                                # I2C address (bus 2, board 2)
bus4.set_port_direction(0, 0x00)                 # 0: pins 1-8, 0x00: set port direction as output
bus4.set_port_direction(1, 0x00)                 # 1: pins 9-16, 0x00: set port direction as output
bus4.write_port(0, 0x00)                         # initially turn off all pins


class ConfirmationPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # function turns off all LEDs when test is ended
        def end_test():

            # makes sure ALL LEDs are OFF when test ends
            for i in range(1, 17):
                bus1.write_pin(i, 0)
                bus2.write_pin(i, 0)
                bus3.write_pin(i, 0)
                bus4.write_pin(i, 0)

            # show next page
            controller.show_frame("TestCompletePage")

        # label for confirmation
        Label(self, text="Are You Sure You Want To End The Test?", font='Arial 20 bold',).place(relx=0.5,
                                                                                                rely=0.1, anchor='n')
        # button to finish test
        Button(self, text="Yes.\nI am finished.", fg="black", font="Arial 14 bold", width="25", height="3",
               bg="#47d147", command=end_test).place(relx=.5, rely=.4, anchor=CENTER)

        # button to return to test, shows different page
        Button(self, text="No.\nReturn to test.", fg="black", font="Arial 14 bold", width="25", height="3",
               bg="#ff4d4d", command=lambda: controller.show_frame("QuestionPage")).place(relx=.5, rely=.7,
                                                                                          anchor=CENTER)
