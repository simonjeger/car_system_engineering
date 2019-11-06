import numpy as np
import shell
import drive_train



class conversion:

    def __init__(self):
        # Initialize
        self.my_shell = shell.jaguar()
        self.my_drive_train = drive_train.drive_weststart()

        # Specs
        self.consumption = 18   # kWh / 100 km (https://ev-database.org/cheatsheet/energy-consumption-electric-car)
        self.weight = self.my_shell.weight + np.sum(self.my_drive_train.quantity) * self.my_drive_train.weight
        self.range = round(self.my_drive_train.capacity / self.consumption * 100, 1)   # km

        # Error
        self.error_weight()
        self.error_volume()


    def error_weight(self):
        if self.weight <= self.my_shell.weight_max:
            return 0
        else:
            print(str(__class__.__name__) + ': error_weight')


    def error_volume(self):
        quantity = [[1 for i in range(6)] for j in range(len(self.my_shell.free_space))]
        option = [[0,1,2], [2,0,1], [1,2,0], [2,1,0], [1,0,2], [0,2,1]]
        for k in range(len(self.my_shell.free_space)):
            for j in range(6):
                for i in range(3):
                    quantity[k][j] = quantity[k][j] * int(self.my_shell.free_space[k][i] / self.my_drive_train.dimension[option[j][i]])

        quantity_max = [0] * len(self.my_shell.free_space)
        for i in range(len(self.my_shell.free_space)):
            quantity_max[i] = np.max(quantity[i])

        if np.sum(quantity_max) >= np.sum(self.my_drive_train.quantity):
            return 0
        else:
            print(str(__class__.__name__) + ': error_volume')
            print('\n')


    def display(self):
        # Name
        print('-----------------------------------------')
        print('system: ' + __class__.__name__)
        print('- - - - - - - - - - - - - - - - - - - - -')

        # Specs
        print('my_shell: ' + str(self.my_shell.__class__.__name__))
        print('my_drive_train: ' + str(self.my_drive_train.__class__.__name__))
        print('consumption: ' + str(self.consumption) + ' [kWh / 100 km]')
        print('weight: ' + str(self.weight) + ' [kg]')
        print('range: ' + str(self.range) + ' [km]')
        print('\n')

my_conversion = conversion()
my_conversion.display()
my_conversion.my_drive_train.display()