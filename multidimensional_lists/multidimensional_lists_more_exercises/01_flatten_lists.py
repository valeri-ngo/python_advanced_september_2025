row = input().split("|")

matrix = [el.strip().split() for el in row]

flattened = [num for el in reversed(matrix) for num in el]
print(" ".join(flattened))