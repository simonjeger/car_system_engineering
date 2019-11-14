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
        self.voltage_min = self.quantity_battery[-1] * self.my_battery.voltage_min
        self.voltage_nom = self.quantity_battery[-1] * self.my_battery.voltage_nom
        self.voltage_max = self.quantity_battery[-1] * self.my_battery.voltage_max

        # Error
        self.error_voltage()


    def error_voltage(self):
        if self.voltage_max <= self.my_motor.voltage_max:
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
        string = string + 'my_motor: ' + self.my_motor.name + '\n'
        string = string + 'my_battery: ' + self.my_battery.name + '\n'
        string = string + 'quantity: ' + str(self.quantity_battery) + '\n'
        string = string + 'weight: ' + str(round(self.weight,1)) + ' [kg]' + '\n'
        string = string + 'dimension: ' + str(self.dimension) + ' [m]' + '\n'
        string = string + 'capacity: ' + str(round(self.capacity,1)) + ' [kWh]' + '\n'
        string = string + 'voltage_min: ' + str(round(self.voltage_min,1)) + ' [V]' + '\n'
        string = string + 'voltage_nom: ' + str(round(self.voltage_nom,1)) + ' [V]' + '\n'
        string = string + 'voltage_max: ' + str(round(self.voltage_max,1)) + ' [V]' + '\n'
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



tesla = drive_train('tesla', MOTOR.ev_hype_high, BATTERY.tesla, [6] * 1)
po4 = drive_train('po4', MOTOR.ev_hype_high, BATTERY.life_po4, [25] * 2)
weststart = drive_train('weststart', MOTOR.ev_hype_high, BATTERY.weststart, [42] * 2)
lfp = drive_train('lfp', MOTOR.ev_hype_high, BATTERY.lfp, [49] * 2)