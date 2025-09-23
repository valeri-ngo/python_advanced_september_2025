row, col = [int(x) for x in input().split()]

matrix = []

for _ in range(row):
    row_data = [x for x in input().split()]
    matrix.append(row_data)

count = 0

for row_index in range(row - 1):
    for col_index in range(col - 1):
        curr_el = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        element_below = matrix[row_index + 1][col_index]
        element_diagonal = matrix[row_index + 1][col_index + 1]

        if curr_el == next_element == element_below == element_diagonal:
            count += 1

print(count)