class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 500
        self.fuel_tank = False

    def get_descriptive_name(self):
        # Method to show specs of a car
        print(f"{self.make} {self.model} {self.year}")

    def incriment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("you cannot roll back an odometer")

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you cannot roll back an odometer")

    def read_fuel_tank(self):
        if self.fuel_tank == False:
            print("Your fuel tank is empty!")
        else:
            print("Your fuel tank is full.")

    def fill_tank(self):
        if self.fuel_tank == True:
            print("Your tank is already full.")
        else:
            print("Your tank is now full.")
            self.fuel_tank = True


class ElectricCar(Car):
    # This child class inherits all of the attributes of its parent's class which in this case is the Car class

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("Electric cars have no fuel tanks!")

    def read_fuel_tank(self):
        print("Electric cars have no fuel tanks!")


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def desc_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        distance = self.battery_size * 3.75
        print(f"This car can go around {distance} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size <= 65:
            self.battery_size = 65
            print("Your battery has been upgraded.")
        else:
            print("your battery has already been upgraded.")


# my_new_car = Car("Audi", "A4", "2024")
# my_new_car.get_descriptive_name()
# my_new_car.update_odometer(400)
# my_new_car.read_odometer()

# used_car = Car("Subaru", "Outback", "2019")
# used_car.update_odometer(23500)
# used_car.read_odometer()

# used_car.incriment_odometer(-500)
# print("after updating odometer")
# used_car.read_odometer()

# my_tesla = ElectricCar("Tesla", "Y-model", 2023)
# my_tesla.get_descriptive_name()
# my_tesla.read_odometer()
# my_tesla.battery.desc_battery()
# my_tesla.battery.get_range()

# my_new_car = Car("Audi", "A4", "2024")
# my_new_car.get_descriptive_name()
# my_new_car.read_fuel_tank()
# my_new_car.fill_tank()
# my_new_car.read_fuel_tank()

# my_tesla = ElectricCar("Tesla", "Y-model", 2023)
# my_tesla.get_descriptive_name()
# my_tesla.battery.desc_battery()
# my_tesla.battery.get_range()
# print("*************************")
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.desc_battery()
# my_tesla.battery.get_range()
