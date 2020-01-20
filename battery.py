import os
import numpy as np



class battery:
    def __init__(self, name, weight, price, dimension, energy, voltage):

        # Initialize

        # Specs
        self.name = name
        self.weight = weight  # kg
        self.price = price # CHF
        self.dimension = dimension  # m
        self.capacity = energy    # kWh
        self.voltage_min = voltage[0]  # V
        self.voltage_nom = voltage[1]  # V
        self.voltage_max = voltage[2]  # V

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
        string = string + 'price: ' + str(round(self.price, 2)) + ' [CHF]' + '\n'
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



tesla = battery('tesla', 25, 1200, [0.685, 0.3, 0.075], 5.3*(1-0.05), [19.6, 22, 24.9]) # the 22 is guessed, I couln't find it on EV europe
westart = battery('westart', 2.55, 6000/40, [0.252, 0.141, 0.043], 0.444, [3, 3.7, 4.2])
life_po4= battery('life_po4', 5.8125, 157.5, [0.28, 0.209, 0.065], 0.5125, [2.8, 3.2, 4])
#lfp = battery('lfp', 3.98, [0.252, 0.141, 0.072], 0.63, [2.5, 3.2, 3.65])