import os
import numpy as np
import BATTERY
import MOTOR



class drive_train:

    def __init__(self, name, my_motor, my_battery, quantity_battery):

        # Initialize
        self.my_motor = my_motor
        self.my_battery = my_battery

        # Specs
        self.name = name
        self.quantity_battery = quantity_battery   # scalar
        self.weight = self.my_battery.weight + self.my_motor.weight
        self.dimension = self.my_battery.dimension
        self.capacity = np.sum(self.quantity_battery) * self.my_battery.capacity
        self.voltage = self.quantity_battery[-1] * self.my_battery.voltage

        # Error
        self.error_voltage()


    def error_voltage(self):
        if self.voltage <= self.my_motor.voltage_max:
            return 0
        else:
            print(str(__class__.__name__) + ': error_voltage')


    def specifications(self):

        # Initialize
        string = ''

        # Name
        string = string + '-----------------------------------------' + '\n'
        string = string + __class__.__name__ + ': ' + self.name + '\n'
        string = string + '- - - - - - - - - - - - - - - - - - - - -' + '\n'

        # Specs
        string = string + 'my_motor: ' + self.my_battery.__class__.__name__ + '\n'
        string = string + 'my_battery: ' + self.my_battery.__class__.__name__ + '\n'
        string = string + 'quantity: ' + str(self.quantity_battery) + '\n'
        string = string + 'weight: ' + str(self.weight) + ' [kg]' + '\n'
        string = string + 'dimension: ' + str(self.dimension) + ' [m]' + '\n'
        string = string + 'capacity: ' + str(self.capacity) + ' [kWh]' + '\n'
        string = string + 'voltage: ' + str(self.voltage) + ' [V]' + '\n'
        string = string + '\n' + '\n'

        return string


    def display(self):
        print(self.specifications())


    def write(self):
        # Clear file
        file = open(self.path + '/' + __class__.__name__ + ".txt", "w")
        file.close()
        os.remove(self.path + '/' + __class__.__name__ + ".txt")

        # Write file
        file = open(self.path + '/' + __class__.__name__ + ".txt", "w")
        file.write(self.specifications())
        file.close()



telsa = drive_train('tesla', MOTOR.ev_hype_low, BATTERY.tesla, [5] * 1)
po4 = drive_train('po4', MOTOR.ev_hype_low, BATTERY.life_po4, [25] * 2)
weststart = drive_train('weststart', MOTOR.ev_hype_low, BATTERY.weststart, [35] * 3)