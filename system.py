import os
import numpy as np
import SHELL
import DRIVE_TRAIN



class conversion:

    def __init__(self, name, my_shell, my_drive_train, consumption):

        # Generate folder for results (only for highest level file)
        self.path = 'specifications'
        os.makedirs(self.path, exist_ok=True)

        # Initialize
        self.my_shell = my_shell
        self.my_drive_train = my_drive_train

        # Specs
        self.name = name
        self.consumption = consumption   # kWh / 100 km (https://ev-database.org/cheatsheet/energy-consumption-electric-car)
        self.weight = self.my_shell.weight + self.my_drive_train.weight
        self.range = self.my_drive_train.capacity / self.consumption * 100  # km

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

        if np.sum(quantity_max) >= np.sum(self.my_drive_train.quantity_battery):
            return 0
        else:
            print(str(__class__.__name__) + ': error_volume')
            print('\n')


    def specifications(self):

        # Initialize
        string = ''

        # Name
        string = string + '-----------------------------------------' + '\n'
        string = string + __class__.__name__ + ': ' + self.name + '\n'
        string = string + '- - - - - - - - - - - - - - - - - - - - -' + '\n'

        # Specs
        string = string + 'my_shell: ' + str(self.my_shell.__class__.__name__) + '\n'
        string = string + 'my_drive_train: ' + str(self.my_drive_train.__class__.__name__) + '\n'
        string = string + 'consumption: ' + str(round(self.consumption,1)) + ' [kWh / 100 km]' + '\n'
        string = string + 'weight: ' + str(round(self.weight,1)) + ' [kg]' + '\n'
        string = string + 'range: ' + str(round(self.range,1)) + ' [km]' + '\n'
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


    def write_all(self):
        # (Only for highest level file)

        # Clear file
        file = open(self.path + "/overall.txt", "w")
        file.close()
        os.remove(self.path + "/overall.txt")

        # Write file
        file = open(self.path + "/overall.txt", "w")
        file.write(self.specifications())
        file.write(self.my_shell.specifications())
        file.write(self.my_drive_train.specifications())
        file.write(self.my_drive_train.my_motor.specifications())
        file.write(self.my_drive_train.my_battery.specifications())
        file.close()



my_conversion = conversion('jaguar', SHELL.jaguar, DRIVE_TRAIN.po4, 18)
my_conversion.write_all()