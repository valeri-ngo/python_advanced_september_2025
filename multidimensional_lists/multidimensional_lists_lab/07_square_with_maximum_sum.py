row, col = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(row):
    row_data = [int(x) for x in input().split(", ")]
    matrix.append(row_data)

max_sum = -9999999999999
sub_matrix = []

for row_index in range(row -1):
    for col_index in range(col -1):
        curr_el = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        element_below = matrix[row_index + 1][col_index]
        element_diagonal = matrix[row_index + 1][col_index + 1]

        current_sum = curr_el + next_element + element_below + element_diagonal

        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [[curr_el, next_element], [element_below, element_diagonal]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)