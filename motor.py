import os
import numpy as np



class motor:
    def __init__(self, name, weight, price, power, torque, voltage_min, voltage_max, ampere_max):

        # Initialize

        # Specs
        self.name = name
        self.weight = weight # kg
        self.price = price # CHF
        self.power = power # W
        self.torque = torque # NM
        self.voltage_min = voltage_min  # V
        self.voltage_max = voltage_max  # V
        self.ampere_max = ampere_max  # A

        # Error



    def specifications(self):

        # Initialize
        string = ''

        # Name
        string = string + '-----------------------------------------' + '\n'
        string = string + __class__.__name__ + ': ' + self.name + '\n'
        string = string + '- - - - - - - - - - - - - - - - - - - - -' + '\n'

        # Specs
        string = string + 'weight: ' + str(round(self.weight, 1)) + ' [kg]' + '\n'
        string = string + 'price: ' + str(round(self.price, 2)) + ' [CHF]' + '\n'
        string = string + 'power: ' + str(round(self.power,1)) + ' [W]' + '\n'
        string = string + 'torque: ' + str(round(self.torque, 1)) + ' [NM]' + '\n'
        string = string + 'voltage_min: ' + str(round(self.voltage_min, 1)) + ' [V]' + '\n'
        string = string + 'voltage_max: ' + str(round(self.voltage_max,1)) + ' [V]' + '\n'
        string = string + 'ampere_max: ' + str(round(self.voltage_max, 1)) + ' [A]' + '\n'
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



ev_hype_low = motor('ev_hype_low', 75, 7166, 112800, 235.1, 62, 130, 650)
ev_hype_high = motor('ev_hype_high', 75, 7383, 90000, 220.7, 90, 180, 500)