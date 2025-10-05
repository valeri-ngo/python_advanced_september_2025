import os

files = {}
directory = "../"

def get_files(folder, level):
    if level == -1:
        return

    for element in os.listdir(folder):
        file = os.path.join(folder, element)
        if os.path.isfile(file):
            extension = os.path.splitext(element)[1]   # element.split(".")[-1]
            if extension not in files:
                files[extension] = []
            files[extension].append(element)
        else:
            get_files(file, level - 1)

get_files(directory, 1)

with open(os.path.join(directory, "report.txt"), "w")as output_file:

    for ext, file_names in sorted(files.items()):
        output_file.write(f".{ext}\n")

        for file_name in sorted(file_names):
            output_file.write(f"- - - {file_name}\n")