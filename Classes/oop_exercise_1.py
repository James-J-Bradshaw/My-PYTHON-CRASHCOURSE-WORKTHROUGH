class Resturant:

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_resturant(self):
        print(
            f"You heard of a resturant called {self.name}, \nthe food is {self.cuisine}, it's great."
        )

    def resturant_open(self):
        print(f"{self.name} just opened, imma get some {self.cuisine}.")

    def customer_report(self):
        print(f"{self.name} has fed {self.number_served} happy customers.")

    def update_customer_number(self, new_customers):
        if new_customers >= self.number_served:
            self.number_served = new_customers
        else:
            print("You cannot turn back this count")

    def incriment_number_served(self, new_customers):
        if new_customers >= 0:
            self.number_served += new_customers
        else:
            print("You cannot turn back this count")


class IceCreamStand(Resturant):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavours = ["chocolate", "vanilla", "peanut"]

    def desc_flavours(self):
        print(f"Our ice cream flavours are:")
        for flavour in self.flavours:
            print(flavour)


class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def desc_user(self):
        print(f"This user's name is {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Greetings {self.first_name}!")

    def incriment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.privilages = ["Can add post", "Can delete post"]

    def desc_privilages(self):
        print(f"Your privilages are:")
        for privilage in self.privilages:
            print(privilage)


# Task 1
# resturant_a = Resturant("New World", "chinese")
# resturant_b = Resturant("TR SPICE", "carribean")
# resturant_c = Resturant("MY Felafel", "KEBAB")

# resturant_a.describe_resturant()
# resturant_b.describe_resturant()
# resturant_c.describe_resturant()

# Task 2
# user_a = User("James", "Bradshaw")
# user_a.desc_user()
# user_a.greet_user()

# print("**********************")
# user_b = User("Elliot", "Jones")
# user_b.desc_user()
# user_b.greet_user()

# print("**********************")
# user_c = User("Chris", "Ashley")
# user_c.desc_user()
# user_c.greet_user()

# Task 3
# resturant_a = Resturant("New World", "chinese")
# resturant_a.customer_report()
# resturant_a.update_customer_number(100)
# resturant_a.incriment_number_served(10)
# print("after updating customer number")
# resturant_a.customer_report()

# Task 4
# user = User("James", "Bradshaw")
# user.incriment_login_attempts()
# print(user.login_attempts)
# user.incriment_login_attempts()
# print(user.login_attempts)
# user.incriment_login_attempts()
# print(user.login_attempts)
# user.incriment_login_attempts()
# print(user.login_attempts)
# user.reset_login_attempts()
# print(user.login_attempts)

# Task 5
# my_stand = IceCreamStand("James' Cream", "Ice Cream")
# my_stand.describe_resturant()
# my_stand.desc_flavours()

# Task 6
# user_a = Admin("James", "Bradshaw")
# user_a.desc_user()
# user_a.desc_privilages()
