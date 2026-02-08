from pathlib import Path

#   Reading from file to python so it can be manipulated

# path = Path("text_files/pi_digits.txt")
# contents = path.read_text()
# lines = contents.splitlines()
# pi_str = ""
# for line in lines:
#     pi_str = pi_str + line
# print(pi_str)
# print(len(pi_str))

#   Writing from python into a file

path = Path("text_files/writing_text.txt")
path.write_text("I love programming!")