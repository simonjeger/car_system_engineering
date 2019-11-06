import numpy as np



class jaguar:

    def __init__(self):
        # Initialize

        # Specs
        self.weight_kerb = 1245 # kg
        self.weight_removed = 200   # kg
        self.weight = self.weight_kerb - self.weight_removed  # kg
        self.weight_max = 1500  # kg
        self.free_space = [[0.95, 0.7, 0.2], [0.6, 0.5, 0.4]]    # m

        # Error


    def display(self):
        # Name
        print('-----------------------------------------')
        print('shell: ' + __class__.__name__)
        print('- - - - - - - - - - - - - - - - - - - - -')

        # Specs
        print('weight kerb: ' + str(self.weight_kerb) + ' [kg]')
        print('weight_removed: ' + str(self.weight_removed) + ' [kg]')
        print('weight: ' + str(self.weight) + ' [kg]')
        print('weight_max: ' + str(self.weight_max) + ' [kg]')
        print('free_space: ' + str(self.free_space) + ' [m]')
        print('\n')