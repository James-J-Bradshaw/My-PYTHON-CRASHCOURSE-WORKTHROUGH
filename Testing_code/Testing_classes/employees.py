class Employee:
    def __init__(self,first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
    
    def give_raise(self):
        while True:
            choice = input(f"""Press '1' to give {self.first} {self.last} an increase of 5000
Press '2' to give {self.first} {self.last} a different increase on their annual wage
Press 'q' to quit program: """)
            if choice == "q":
                break

            if choice == "1":
                self.salary = self.salary + 5000
                print(f"{self.first}'s anual salary is now {self.salary}")
                break

            if choice == "2":
                while True:
                    increase = input("Enter increase amount: ")
                    try:
                        increase.rstrip()
                        increase = int(increase)
                        self.salary = self.salary + increase
                        print(f"{self.first}'s anual salary is now {self.salary}")
                        break
                    except ValueError:
                        print("What was entered was not a number")
            else:
                print("Please enter '1' or '2' to proceed, or press 'q' to leave program.")
                

me = Employee("James", "Bradshaw", 7500)
me.give_raise()