from pathlib import Path
# 10.1
# path = Path("../text_files/learning_python.txt")
# contents = path.read_text()
# lines = contents.splitlines()
# string = ""
# for line in lines:
#     string = string + line + " "
# print(string)
# print(len(string))

# 10.2 I
# path = Path("../text_files/file_exception_exercises.txt")
# contents = path.read_text()
# contents = contents.replace("dogs", "cats")
# print(contents)

# 10.2 II

# path= Path("../text_files/learning_python.txt")
# contents = path.read_text()
# contents = contents.replace("python", "C")
# print(contents)

# 10.4
# path = Path("../text_files/guest.txt")
# contents = path.read_text()
# contents = contents.rstrip()
# name = input("What is your name for the guest book? ")
# contents = contents.__add__("\n" + name)
# print (f"The guest list is: \n{contents}")
# path.write_text(contents)

# 10.10
def counter(file):
    path = Path(file)
    contents = path.read_text()
    count = contents.lower().count("cream")
    return count

count = counter("../text_files/repetitive.txt")
print(f"This file says cream {count} times.")