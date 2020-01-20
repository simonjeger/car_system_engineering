import os
import numpy as np



class shell:

    def __init__(self, name, weight_kerb, weight_removed, weight_max, price, free_space):

        # Initialize

        # Specs
        self.name = name
        self.weight_kerb = weight_kerb # kg
        self.weight_removed = weight_removed   # kg
        self.weight = self.weight_kerb - self.weight_removed  # kg
        self.weight_max = weight_max  # kg
        self.price = price
        self.free_space = free_space    # m

        # Error



    def specifications(self):

        # Initialize
        string = ''

        # Name
        string = string + '-----------------------------------------' + '\n'
        string = string + __class__.__name__ + ': ' + self.name + '\n'
        string = string + '- - - - - - - - - - - - - - - - - - - - -' + '\n'

        # Specs
        string = string + 'weight_kerb: ' + str(round(self.weight_kerb,1)) + ' [kg]' + '\n'
        string = string + 'weight_removed: ' + str(round(self.weight_removed,1)) + ' [kg]' + '\n'
        string = string + 'weight: ' + str(round(self.weight,1)) + ' [kg]' + '\n'
        string = string + 'weight_max: ' + str(round(self.weight_max,1)) + ' [kg]' + '\n'
        string = string + 'price: ' + str(round(self.price, 2)) + ' [CHF]' + '\n'
        string = string + 'free_space: ' + str(self.free_space) + ' [m]' + '\n'
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

#jaguar_small = shell('jaguar_short', 1245, 150, 1500, 40000, [[0.4, 0.387, 0.500], [0.935, 0.63, 0.178]])
#jaguar = shell('jaguar', 1245, 150, 1500, 40000, [[0.4, 0.387, 0.500], [0.935, 0.315, 0.218], [0.935, 0.315, 0.178]])
#jaguar_nose = shell('jaguar_nose', 1245, 150, 1500, 40000, [[0.45, 0.30, 0.500], [0.4, 0.387, 0.500], [0.935, 0.315, 0.218], [0.935, 0.315, 0.178]])
#jaguar_ext = shell('jaguar_ext', 1245, 150, 1500, 40000, [[0.4, 0.387, 0.500], [0.935, 0.63, 0.255]])
jaguar_front_back = shell('jag_front_back', 1245, 150, 1500, 40000, [[0.45, 0.30, 0.500], [0.4, 0.387, 0.500], [0.935, 0.63, 0.255]])
#jaguar_ground_back = shell('jag_ground_back', 1245, 150, 1500, 40000, [[2.4, 1, 0.08], [0.935, 0.63, 0.255]])
vw = shell('vw', 1285, 150, 2250, 0, [[1.50, 1.05, .28]])