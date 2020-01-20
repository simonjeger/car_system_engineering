import os
import numpy as np



class miscellaneous:
    def __init__(self, name, power_max):

        # Initialize

        # Specs
        self.name = name
        self.price = 10890 # CHF Tesla kit - 10x Tesla Batterie - 1x Motor

        # Error



    def specifications(self):
        # Initialize
        string = ''

        # Name
        string = string + '-----------------------------------------' + '\n'
        string = string + __class__.__name__ + ': ' + self.name + '\n'
        string = string + '- - - - - - - - - - - - - - - - - - - - -' + '\n'

        # Specs
        string = string + 'price: ' + str(round(self.price, 2)) + ' [CHF]' + '\n'
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



ev_miscellaneous = miscellaneous('ev_miscellaneous', 10)