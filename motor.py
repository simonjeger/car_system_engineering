import numpy as np



class ev_hype_low:
    def __init__(self):
        # Initialize

        # Specs
        self.power = 90 #kV
        self.voltage_max = 130  # V

        # Error


    def display(self):
        # Name
        print('-----------------------------------------')
        print('motor: ' + __class__.__name__)
        print('- - - - - - - - - - - - - - - - - - - - -')

        # Specs
        print('power: ' + str(self.power) + ' [V]')
        print('voltage_max: ' + str(self.voltage_max) + ' [V]')
        print('\n')