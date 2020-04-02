class Bus(object):
    def __init__(self, bus_number):
        self.bus_number = bus_number
        bus_num = hex(self.bus_number)
        print('Bus created:', bus_num)

    def write_pin(self, pin_number, state):
        print('SIMULATION')
        bus_num = hex(self.bus_number)
        print('Bus:', bus_num)  # COMMENT WHEN USING HARDWARE
        print('Pin:', pin_number)  # COMMENT WHEN USING HARDWARE

        if state:
            print('ON')

        else:
            print('OFF')

        print('------')

    def set_port_direction(self, a, b):
        print('Write port direction')  # (0, 0x00)

    def write_port(self, a, b):
        bus_num = hex(self.bus_number)
        print('Write port', bus_num)    # (0, 0x00)

