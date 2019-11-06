import numpy as np



class tesla:
    def __init__(self):
        # Initialize

        # Specs
        self.weight = 25  # kg
        self.dimension = [0.7, 0.31, 0.08]    # m
        self.capacity = 5.3    # kWh
        self.voltage = 24.9  # V

        # Error


    def display(self):
        # Name
        print('-----------------------------------------')
        print('battery: ' + __class__.__name__)
        print('- - - - - - - - - - - - - - - - - - - - -')

        # Specs
        print('weight: ' + str(self.weight) + ' [kg]')
        print('dimension: ' + str(self.dimension) + ' [m]')
        print('capacity: ' + str(self.capacity) + ' [kWh]')
        print('voltage: ' + str(self.voltage) + ' [V]')
        print('\n')



class life_po4:
    def __init__(self):
        # Initialize

        # Specs
        self.weight = 5.8125  # kg
        self.dimension = [0.28, 0.19, 0.075]  # m
        self.capacity = 0.5125  # kWh
        self.voltage = 3.2  # V

        # Error


    def display(self):
        # Name
        print('-----------------------------------------')
        print('battery: ' + __class__.__name__)
        print('- - - - - - - - - - - - - - - - - - - - -')

        # Specs
        print('weight: ' + str(self.weight) + ' [kg]')
        print('dimension: ' + str(self.dimension) + ' [m]')
        print('capacity: ' + str(self.capacity) + ' [kWh]')
        print('voltage: ' + str(self.voltage) + ' [V]')
        print('\n')



class weststart:
    def __init__(self):
        # Initialize

        # Specs
        self.weight = 2.55  # kg
        self.dimension = [0.252, 0.141, 0.041]  # m
        self.capacity = 0.5125  # kWh
        self.voltage = 3.7  # V

        # Error


    def display(self):
        # Name
        print('-----------------------------------------')
        print('battery: ' + __class__.__name__)
        print('- - - - - - - - - - - - - - - - - - - - -')

        # Specs
        print('weight: ' + str(self.weight) + ' [kg]')
        print('dimension: ' + str(self.dimension) + ' [m]')
        print('capacity: ' + str(self.capacity) + ' [kWh]')
        print('voltage: ' + str(self.voltage) + ' [V]')
        print('\n')