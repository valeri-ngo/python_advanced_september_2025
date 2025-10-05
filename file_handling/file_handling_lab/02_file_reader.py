import os

path = os.path.join("../file_handling_txt_files/02_file_reader", "numbers.txt")

file = open(path)

numbers = [int(x) for x in file.read().split('\n')]

print(sum(numbers))
