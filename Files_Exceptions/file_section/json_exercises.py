from pathlib import Path
import json

# 10.11
# path = Path("../json_files/fav_number.json")
# def input_number(path):
#     number = input("tell me your favourite number? ")
#     path = Path(path)
#     contents = json.dumps(number)
#     path.write_text(contents)
#     print("Your number has been saved")

# def read_number(path):
#     path = Path(path)
#     contents = path.read_text()
#     number = json.loads(contents)
#     print(f"I know your fav number, it is {number}")

# 10.12
# path = Path("../json_files/fav_number.json")

# def input_or_read_number(path):
#     path = Path(path)
#     contents = path.read_text()
#     if contents == "":
#         input_num(path)        
#     try:
#         number = int(contents)
#         print(f"I know your fav number, it is {number}")

#     except ValueError:
#         input_num(path)
    
# def input_num(file):
#     while True:
#         number = input("tell me your favourite number? ")
#         try:
#             number = int(number)
#             break
#         except ValueError:
#             print("I believe that was not a number")
#     path = Path(file)
#     contents = json.dumps(number)
#     path.write_text(contents)
#     print("Your number has been saved")


# input_or_read_number(path)

# 10.13

# path = Path("../json_files/username.json")

# def dump_info(path):
#     info = {}
#     username = input("What is your name? ")
#     while True:
#         age = input("What is your age? ")
#         try:
#             age = int(age)
#             break
#         except ValueError:
#             print("I believe that was not a number...")
        
#     postcode = input("What is your postcode? ")
#     info["Username"] = username
#     info["Age"] = age
#     info["Postcode"] = postcode
#     path = Path(path)
#     contents = json.dumps(info)
#     path.write_text(contents)
#     print(f"We'll remember you when you come back, {username}.")

# def load_info(path):
#     path = Path(path)
#     contents = path.read_text()
#     info = json.loads(contents)
#     print(f"""
#           With the information you gave us, We believe your name is {info["Username"]},
#           your age is {info["Age"]}, and you live in the area of {info["Postcode"]}
#           """)

# def main(path):
#     path = Path(path)
#     if path.exists() == True:
#         contents = path.read_text()
#         length = len(contents)
#         if length == 0:
#             dump_info(path)
#         else:
#             load_info(path)
#     else:
#         dump_info(path)

# main(path)

# 10.14

path = Path("../json_files/username.json")

def dump_info(path):
    info = {}
    username = input("What is your name? ")
    while True:
        age = input("What is your age? ")
        try:
            age = int(age)
            break
        except ValueError:
            print("I believe that was not a number...")
        
    postcode = input("What is your postcode? ")
    info["Username"] = username
    info["Age"] = age
    info["Postcode"] = postcode
    path = Path(path)
    contents = json.dumps(info)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}.")

def load_info(path):
    path = Path(path)
    contents = path.read_text()
    info = json.loads(contents)
    print(f"""
          With the information you gave us, We believe your name is {info["Username"]},
          your age is {info["Age"]}, and you live in the area of {info["Postcode"]}
          """)

def main(path):
    path = Path(path)
    if path.exists() == True:
        contents = path.read_text()
        length = len(contents)
        if length == 0:
            dump_info(path)
        else:
            verify(path)
    else:
        dump_info(path)

def verify(path):
    path = Path(path)
    contents = path.read_text()
    info = json.loads(contents)
    ans = input(f"Just to check,  is this {info["Username"]}?\n y/n yes or no: ")
    if ans == "y":
        load_info(path)
    elif ans == "n":
        dump_info(path)
    else:
        print(f"y or n is needed to verify that you are {info["Username"]} or not..\n Press y or n. ")    


main(path)