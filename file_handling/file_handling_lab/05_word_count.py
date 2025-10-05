import os.path
import re

path = os.path.join('..', 'file_handling_txt_files', '05_word_count')

with open(os.path.join(path, 'text.txt'))as file:
    text = file.read()

with open(os.path.join(path, "words.txt")) as file:
    words = file.read().split()

data = {}

for word in words:
   pattern =  rf"\b{word}\b"
   result = len(re.findall(pattern, text, re.IGNORECASE))
   data[word] = result

sorted_data = sorted(data.items(), key=lambda kvp: -kvp[1])

with open(os.path.join(path, "output.txt"), "w") as file:
    for key, value in sorted_data:
        file.write(f"{key} - {value}\n")