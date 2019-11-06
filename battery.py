import os
import numpy as np



class battery:
    def __init__(self, name, weight, dimension, capacity, voltage):

        # Initialize

        # Specs
        self.name = name
        self.weight = weight  # kg
        self.dimension = dimension  # m
        self.capacity = capacity    # kWh
        self.voltage = voltage  # V

        # Error



    def specifications(self):
        # Initialize
        string = ''

        # Name
        string = string + '-----------------------------------------' + '\n'
        string = string + __class__.__name__ + ': ' + self.name + '\n'
        string = string + '- - - - - - - - - - - - - - - - - - - - -' + '\n'

        # Specs
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



tesla = battery('tesla', 25, [0.7, 0.31, 0.08], 5.3, 24.9)
life_po4= battery('life_po4', 5.8125, [0.28, 0.19, 0.075], 0.5125, 3.2)
weststart = battery('weststart', 2.55, [0.252, 0.141, 0.041], 0.5125, 3.7)