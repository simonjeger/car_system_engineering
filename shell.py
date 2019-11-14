import os
import numpy as np



class shell:

    def __init__(self, name, weight_kerb, weight_removed, weight_max, free_space):

        # Initialize

        # Specs
        self.name = name
        self.weight_kerb = weight_kerb # kg
        self.weight_removed = weight_removed   # kg
        self.weight = self.weight_kerb - self.weight_removed  # kg
        self.weight_max = weight_max  # kg
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
        string = string + 'weight kerb: ' + str(round(self.weight_kerb,1)) + ' [kg]' + '\n'
        string = string + 'weight_removed: ' + str(round(self.weight_removed,1)) + ' [kg]' + '\n'
        string = string + 'weight: ' + str(round(self.weight,1)) + ' [kg]' + '\n'
        string = string + 'weight_max: ' + str(round(self.weight_max,1)) + ' [kg]' + '\n'
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



jaguar = shell('jaguar', 1245, 200, 1500, [[0.95, 0.7, 0.2], [0.6, 0.5, 0.4]])