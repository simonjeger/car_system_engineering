import os
import numpy as np



class charging:
    def __init__(self, name, power_max):

        # Initialize

        # Specs
        self.name = name
        self.price = 1087.25 # CHF https://www.microspot.ch/de/freizeit-sport/mobility/e-mobility-stromversorgung--c890000/green-motion-home-two-ladestation-11kw--p0001899680?gclid=Cj0KCQiAxfzvBRCZARIsAGA7YMxW_V0-U66WU4vT5TwdK3bho5USqk73A4mhHJDrlOfRELPKRNPvtSEaAqD-EALw_wcB&gclsrc=aw.ds
        self.power_max = power_max # A

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
        string = string + 'power_max: ' + str(round(self.ampere_max, 1)) + ' [kW]' + '\n'
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



ev_charging = charging('ev_charging', 10)