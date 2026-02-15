class Employee:
    def __init__(self,first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
    
    def give_default_raise(self):
        """Adds £5000 to their anual salary"""
        self.salary = self.salary + 5000
        print(f"{self.first}'s anual salary is now {self.salary}")

    def give_custom_raise(self, increase):
        numbers = "1234567890"
        increase = str(increase)
        clean_increase = ""
        try:
            for char in increase:
                if char in numbers:
                    clean_increase = clean_increase + char
            increase.rstrip()
            increase = int(clean_increase)
            self.salary = self.salary + increase
            print(f"{self.first}'s anual salary is now {self.salary}")
        except ValueError:
            print("What was entered was not a number")