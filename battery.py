import os
import numpy as np



class battery:
    def __init__(self, name, weight, dimension, energy, voltage):

        # Initialize

        # Specs
        self.name = name
        self.weight = weight  # kg
        self.dimension = dimension  # m
        self.capacity = energy    # kWh
        self.voltage_min = voltage[0]  # V
        self.voltage_nom = voltage[1]
        self.voltage_max = voltage[2]

        # Error



    def specifications(self):
        # Initialize
        string = ''

        # Name
        string = string + '-----------------------------------------' + '\n'
        string = string + __class__.__name__ + ': ' + self.name + '\n'
        string = string + '- - - - - - - - - - - - - - - - - - - - -' + '\n'

        # Specs
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



tesla = battery('tesla', 25, [0.7, 0.31, 0.08], 5.3, [19.6, 22, 24.9]) # the 22 is guessed, I couln't find it on EV europe
life_po4= battery('life_po4', 5.8125, [0.28, 0.19, 0.075], 0.5125, [2.8, 3.2, 4])
weststart = battery('weststart', 2.55, [0.252, 0.141, 0.041], 0.5125, [3, 3.7, 4.2])
lfp = battery('lfp', 3.98, [0.2, 0.174, 0.054], 0.63, [2.5, 3.2, 3.65])