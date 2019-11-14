import os
import numpy as np



class motor:
    def __init__(self, name, weight, power, voltage_max):

        # Initialize

        # Specs
        self.name = name
        self.weight = weight # kg
        self.power = power # kV
        self.voltage_max = voltage_max  # V

        # Error



    def specifications(self):

        # Initialize
        string = ''

        # Name
        string = string + '-----------------------------------------' + '\n'
        string = string + __class__.__name__ + ': ' + self.name + '\n'
        string = string + '- - - - - - - - - - - - - - - - - - - - -' + '\n'

        # Specs
        string = string + 'power: ' + str(round(self.power,1)) + ' [V]' + '\n'
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



ev_hype_low = motor('ev_hype_low', 75, 90, 130)
ev_hype_high = motor('ev_hype_high', 75, 90, 180)