from pathlib import Path

# try:
#   print(5/0)
# except ZeroDivisionError:
#     print("You cannot divide by zero!")

# try:
#     print(hello)
# except NameError:
#     print("that variable does not exist")

# path = Path("../text_files/Alice_in_wonderland.txt")
# try:
#     contents = path.read_text(encoding="utf-8")
# except FileNotFoundError:
#     print(f"Im afraid that the file '{path}' does not exist in this directory. :/")
# else:
#     print(contents)

def count_words_path(path):
    path = Path(path)
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Im afraid that the file '{path}' does not exist in this directory.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} contains {num_words} words.")

filenames = ["../text_files/guest.txt", "../text_files/file_don't_exist.txt", "../text_files/Alice_in_wonderland.txt",]
for files in filenames:
    count_words_path(files)