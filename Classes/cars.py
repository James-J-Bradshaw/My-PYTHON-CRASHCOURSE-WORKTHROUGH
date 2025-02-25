class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 500

    def get_descriptive_name(self):
        # Method to show specs of a car
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name

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


# my_new_car = Car("Audi", "A4", "2024")
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(400)
# my_new_car.read_odometer()

used_car = Car("Subaru", "Outback", "2019")
used_car.update_odometer(23500)
used_car.read_odometer()

used_car.incriment_odometer(-500)
print("after updating odometer")
used_car.read_odometer()
