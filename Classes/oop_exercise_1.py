class Resturant:

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_resturant(self):
        print(
            f"You heard of a resturant called {self.name}, \nthe food is {self.cuisine}, it's great"
        )

    def resturant_open(self):
        print(f"{self.name} just opened, imma get some {self.cuisine}.")


resturant_a = Resturant("New World", "chinese")
resturant_b = Resturant("TR SPICE", "carribean")
resturant_c = Resturant("MY Felafel", "KEBAB")

resturant_a.describe_resturant()
resturant_b.describe_resturant()
resturant_c.describe_resturant()
