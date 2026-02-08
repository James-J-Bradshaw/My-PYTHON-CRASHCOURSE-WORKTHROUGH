from pathlib import Path
import json

# path = Path("../json_files/numbers.json")
# numbers = [2,3,5,7,11,13]
# contents = json.dumps(numbers)
# path.write_text(contents)

# username = input("What is your name? ")
# path = Path("../json_files/username.json")
# contents = json.dumps(username)
# path.write_text(contents)
# print(f"We'll remember you when you come back, {username}")

path = Path("../json_files/username.json")

def dump_username(path):
    username = input("What is your name? ")
    path = Path(path)
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}")

def load_username(path):
    path = Path(path)
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")

if path.exists():
    load_username(path)
else:
    dump_username(path)