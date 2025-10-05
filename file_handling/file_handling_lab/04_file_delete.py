import os

try:
    path = os.path.join('..', 'file_handling_txt_files', '03_file_writer', 'my_first_file.txt')
    os.remove(path)
except FileNotFoundError:
    print("File already deleted")
