import os

path = os.path.join("..", "file_handling_txt_files", "01_file_opener", "text.txt")

try:
    open(path, 'r')
    print("File found")
except FileNotFoundError:
    print("File not found")