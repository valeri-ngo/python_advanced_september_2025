import os

files = {}
directory = "../"

for element in os.listdir(directory):
    file = os.path.join(directory, element)

    if os.path.isfile(file):
        ext = element.split(".")[-1]

        if ext not in files:
            files[ext] = []
        files[ext].append(element)

    else:

        for el in os.listdir(file):
            filename = os.path.join(file, el)

            if os.path.isfile(filename):
                ext = el.split(".")[-1]

                if ext not in files:
                    files[ext] = []
                files[ext].append(el)

with open(os.path.join(directory, "report.txt"), "w")as output_file:

    for ext, file_names in sorted(files.items()):
        output_file.write(f".{ext}\n")

        for file_name in sorted(file_names):
            output_file.write(f"- - - {file_name}\n")