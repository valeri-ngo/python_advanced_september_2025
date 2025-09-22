rows = int(input())

matrix = []

for _ in range(rows):
    cols = [int(x) for x in input().split(", ")]
    matrix.append(cols)
flattened_matrix = [num for row in matrix for num in row]
print(flattened_matrix)