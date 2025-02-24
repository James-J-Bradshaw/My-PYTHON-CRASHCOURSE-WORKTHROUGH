class Dog:
    # simple class to model a dog
    # any function that is part of a class is called a "method"
    def __init__(self, name, age):
        # This section is setting the attributes for our class
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over")


my_dog = Dog("TOBI", 3)
your_dog = Dog("JACKJACK", 5)

print(f"My dog's name is {my_dog.name}.")
print(f"my dog's age is {my_dog.age}.")
my_dog.sit()

print(f"your dog's name is {your_dog.name}.")
print(f"your dog's age is {your_dog.age}.")
your_dog.sit()
