import os
import numpy as np
import BATTERY
import MOTOR



class drive_train:

    def __init__(self, name, my_motor, my_battery, quantity_battery):

        # Initialize
        self.my_motor = my_motor
        self.my_battery = my_battery

        # Specs
        self.name = name
        self.weight = self.my_motor.weight + self.my_battery.weight * np.sum(quantity_battery)  # kg
        self.price = self.my_motor.price + self.my_battery.price * np.sum(quantity_battery) # CHF
        self.quantity_battery = quantity_battery
        self.dimension = self.my_battery.dimension # m
        self.capacity = np.sum(self.quantity_battery) * self.my_battery.capacity
        self.voltage_min = len(self.quantity_battery) * self.my_battery.voltage_min
        self.voltage_nom = len(self.quantity_battery) * self.my_battery.voltage_nom
        self.voltage_max = len(self.quantity_battery) * self.my_battery.voltage_max
        self.cable_diameter = np.sqrt(self.my_motor.ampere_max / (6 / 10e-6) * 4 / np.pi)

        # Error
        self.error_voltage()


    def error_voltage(self):

        if self.voltage_min >= self.my_motor.voltage_min:
            pass
        else:
            print(str(__class__.__name__) + ': error_voltage_min')

        if self.voltage_max <= self.my_motor.voltage_max:
            pass
        else:
            print(str(__class__.__name__) + ': error_voltage_max')


    def specifications(self):

        # Initialize
        string = ''

        # Name
        string = string + '-----------------------------------------' + '\n'
        string = string + __class__.__name__ + ': ' + self.name + '\n'
        string = string + '- - - - - - - - - - - - - - - - - - - - -' + '\n'

        # Specs
        string = string + 'weight: ' + str(round(self.weight, 1)) + ' [kg]' + '\n'
        string = string + 'price: ' + str(round(self.price, 2)) + ' [CHF]' + '\n'
        string = string + 'my_motor: ' + self.my_motor.name + '\n'
        string = string + 'my_battery: ' + self.my_battery.name + '\n'
        string = string + 'quantity: ' + str(self.quantity_battery) + '\n'
        string = string + 'dimension: ' + str(self.dimension) + ' [m]' + '\n'
        string = string + 'capacity: ' + str(round(self.capacity,1)) + ' [kWh]' + '\n'
        string = string + 'voltage_min: ' + str(round(self.voltage_min,1)) + ' [V]' + '\n'
        string = string + 'voltage_nom: ' + str(round(self.voltage_nom,1)) + ' [V]' + '\n'
        string = string + 'voltage_max: ' + str(round(self.voltage_max,1)) + ' [V]' + '\n'
        string = string + 'cable_diameter: ' + str(round(self.cable_diameter, 3)) + ' [m]' + '\n'
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



#jag_tesla = drive_train('tesla', MOTOR.ev_hype_low, BATTERY.tesla, [3] * 4)
jag_westart = drive_train('westart', MOTOR.ev_hype_low, BATTERY.westart, [4] * 29)
#jag_westart_ground = drive_train('westart', MOTOR.ev_hype_low, BATTERY.westart, [4] * 35)
#vw_tesla = drive_train('tesla', MOTOR.ev_hype_high, BATTERY.tesla, [7] * 2)
vw_westart = drive_train('westart', MOTOR.ev_hype_high, BATTERY.westart, [4]*42)
#po4 = drive_train('po4', MOTOR.ev_hype_low, BATTERY.life_po4, [25] * 2)
#lfp = drive_train('lfp', MOTOR.ev_hype_high, BATTERY.lfp, [49] * 2)