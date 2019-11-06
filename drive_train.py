import numpy as np

import battery
import motor


class drive_tesla:

    def __init__(self):
        # Initialize
        self.my_motor = motor.ev_hype_low()
        self.my_battery = battery.tesla()

        # Specs
        self.quantity = [5] * 1   # scalar
        self.weight = self.my_battery.weight
        self.dimension = self.my_battery.dimension
        self.capacity = np.sum(self.quantity) * self.my_battery.capacity
        self.voltage = self.quantity[-1] * self.my_battery.voltage

        # Error
        self.error_voltage()


    def error_voltage(self):
        if self.voltage <= self.my_motor.voltage_max:
            return 0
        else:
            print(str(__class__.__name__) + ': error_voltage')


    def display(self):
        # Name
        print('-----------------------------------------')
        print('drive_train: ' + __class__.__name__)
        print('- - - - - - - - - - - - - - - - - - - - -')

        # Specs
        print('my_motor: ' + str(self.my_battery.__class__.__name__))
        print('my_battery: ' + str(self.my_battery.__class__.__name__))
        print('quantity: ' + str(self.quantity))
        print('weight: ' + str(self.weight) + ' [kg]')
        print('dimension: ' + str(self.dimension) + ' [m]')
        print('capacity: ' + str(self.capacity) + ' [kWh]')
        print('voltage: ' + str(self.voltage) + ' [V]')
        print('\n')



class drive_po4:

    def __init__(self):
        # Initialize
        self.my_battery = battery.life_po4()
        self.my_motor = motor.ev_hype_low()

        # Specs
        self.quantity = [25] * 2  # scalar
        self.weight = self.my_battery.weight
        self.dimension = self.my_battery.dimension
        self.capacity = np.sum(self.quantity) * self.my_battery.capacity
        self.voltage = self.quantity[-1] * self.my_battery.voltage

        # Error
        self.error_voltage()


    def error_voltage(self):
        if self.voltage <= self.my_motor.voltage_max:
            return 0
        else:
            print(str(__class__.__name__) + ': error_voltage')


    def display(self):
        # Name
        print('-----------------------------------------')
        print('drive_train: ' + __class__.__name__)
        print('- - - - - - - - - - - - - - - - - - - - -')

        # Specs
        print('my_motor: ' + str(self.my_motor.__class__.__name__))
        print('my_battery: ' + str(self.my_battery.__class__.__name__))
        print('quantity: ' + str(self.quantity))
        print('weight: ' + str(self.weight) + ' [kg]')
        print('dimension: ' + str(self.dimension) + ' [m]')
        print('capacity: ' + str(self.capacity) + ' [kWh]')
        print('voltage: ' + str(self.voltage) + ' [V]')
        print('\n')



class drive_weststart:

    def __init__(self):
        # Initialize
        self.my_battery = battery.weststart()
        self.my_motor = motor.ev_hype_low()

        # Specs
        self.quantity = [35] * 3  # scalar
        self.weight = self.my_battery.weight
        self.dimension = self.my_battery.dimension
        self.capacity = np.sum(self.quantity) * self.my_battery.capacity
        self.voltage = self.quantity[-1] * self.my_battery.voltage

        # Error
        self.error_voltage()


    def error_voltage(self):
        if self.voltage <= self.my_motor.voltage_max:
            return 0
        else:
            print(str(__class__.__name__) + ': error_voltage')


    def display(self):
        # Name
        print('-----------------------------------------')
        print('drive_train: ' + __class__.__name__)
        print('- - - - - - - - - - - - - - - - - - - - -')

        # Specs
        print('my_motor: ' + str(self.my_motor.__class__.__name__))
        print('my_battery: ' + str(self.my_battery.__class__.__name__))
        print('quantity: ' + str(self.quantity))
        print('weight: ' + str(self.weight) + ' [kg]')
        print('dimension: ' + str(self.dimension) + ' [m]')
        print('capacity: ' + str(self.capacity) + ' [kWh]')
        print('voltage: ' + str(self.voltage) + ' [V]')
        print('\n')