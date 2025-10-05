import os

path = os.path.join('..', 'file_handling_txt_files', '03_file_writer', 'my_first_file.txt')

with open(path, 'w+') as file:
    file.write('I just created my first file!')
