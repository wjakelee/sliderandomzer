class Bus(object):      # used if hardware is not connected
    def __init__(self, bus_number):
        self.bus_number = bus_number
        bus_num = hex(self.bus_number)  # sets bus number to hexi-decimal
        print('Bus created:', bus_num)      # print statement to command window

    # function prints whether pin is on or off
    def write_pin(self, pin_number, state):
        print('SIMULATION')
        bus_num = hex(self.bus_number)      # sets bus number to hexi-decimal
        print('Bus:', bus_num)
        print('Pin:', pin_number)

        if state:
            print('ON')

        else:
            print('OFF')

        print('------')

    # prints port direction
    def set_port_direction(self, a, b):
        print('Write port direction')     # (0, 0x00)

    # prints that all ports are turned off
    def write_port(self, a, b):
        bus_num = hex(self.bus_number)
        print('Write port', bus_num)       # (0, 0x00)

