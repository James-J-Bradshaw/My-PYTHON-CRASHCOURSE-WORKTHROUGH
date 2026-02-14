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
path = Path("../json_files/fav_number.json")

def input_or_read_number(path):
    path = Path(path)
    contents = path.read_text()
    number = json.loads(contents)
    
    
    
    number = input("tell me your favourite number? ")
    path = Path(path)
    contents = json.dumps(number)
    path.write_text(contents)
    print("Your number has been saved")
    
    path = Path(path)
    contents = path.read_text()
    number = json.loads(contents)
    print(f"I know your fav number, it is {number}")



# input_number(path)
# read_number(path)
