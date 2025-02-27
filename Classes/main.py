from cars import *

my_new_car = Car("Audi", "TT", 2020)
my_new_car.get_descriptive_name()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

print("**************")
my_tesla = ElectricCar("Tesla", "Y-model", 2018)
my_tesla.battery.get_range()
