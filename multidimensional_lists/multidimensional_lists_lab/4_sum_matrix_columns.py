row, col = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(row):
    row_data = [int(x) for x in input().split()]
    matrix.append(row_data)

for col_index in range(col):
    col_sum = 0
    for row_index in range(row):
        col_sum += matrix[row_index][col_index]
    print(col_sum)