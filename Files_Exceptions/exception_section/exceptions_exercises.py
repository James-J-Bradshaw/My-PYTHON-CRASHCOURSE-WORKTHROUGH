from pathlib import Path
# 10.6 and 10.7
# print("Give me two numbers, and I will attempt to add them.")
# print("enter 'q' to quit")
# while True:
#     first_num = input("\nFirst number: ")
#     if first_num == "q":
#         break
#     second_num = input("\nSecond number: ")
#     if second_num == "q":
#         break
#     try:
#         answer = int(first_num) + int(second_num)
#     except ValueError:
#         print("you cannot add letters.")
#     else: print(answer)

# 10.8
# def read_pets(path):
#     path = Path(path)
#     try:
#         contents = path.read_text()
#     except FileNotFoundError:
#         print("That file does not exist in this directory")
#     else: 
#         print(contents)

# filenames = ["../text_files/cats.txt", "../text_files/dogs.txt"]
# for file in filenames:
#     read_pets(file)
