from random import randint
# 9.13 Dice
# class Die:
#     def __init__(self, sides):
#         self.sides = sides
    
#     def roll_dice(self):
#         num = 0
#         while num < 10:
#             value = randint(1, self.sides)
#             print(value)
#             num = num + 1

# die = Die(20)
# die.roll_dice()

# 9.14 Lottery
# Lottery = [35,12,23,67,85,6,45,30,90,21,"L", "W", "S", "G", "O"]
# num = 0
# winner = []
# while num < 4:
#     value = randint(0, 14)
#     chosen = Lottery[value]
#     print(chosen)
#     winner.append(chosen)
#     num = num + 1

# print(f"The winning ticket is {winner}")

# 9.15 lottery analysis
# Lottery = [35,12,23,67,85,6,45,30,90,21,"L", "W", "S", "G", "O"]
# my_draw = [12,35,23,67]
# attempts = 0
# simulation = True
# while simulation == True:
#     num = 0
#     winner = []
#     while num < 4:
#         value = randint(0, 14)
#         chosen = Lottery[value]
#         winner.append(chosen)
#         num = num + 1
#     if my_draw == winner:
#         break
#     else:
#         attempts = attempts + 1

# print(f"It took {attempts} amount of tries for you to win the lottery with your numbers")