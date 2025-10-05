# import re

with open("text.txt") as file:

    for row, line in enumerate(file):
        if row % 2 == 0:
            for ele in {"-", ",", ".", "!", "?"}:
                line = line.replace(ele, "@")
            print(" ".join(reversed(line.split())))

    # lines = file.readlines()
    # for i in range(0, len(lines), 2):
    #     line = reversed(re.sub("['-,.!?']", "@", lines[i]).split())
    #     print(*line)