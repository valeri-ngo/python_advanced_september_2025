row, col = [int(x) for x in input().split()]

matrix = []

for _ in range(row):
    row_data = [int(x) for x in input().split()]
    matrix.append(row_data)

best_sum = float('-inf')
best_row = best_col = 0

for row_index in range(row - 2):
    for col_index in range(col - 2):
        block_sum = sum(matrix[row_index + r][col_index + c] for r in range(3) for c in range(3))
        if block_sum > best_sum:
            best_sum = block_sum
            best_row, best_col = row_index, col_index

print(f"Sum = {best_sum}")
for r in range(3):
    print(*[matrix[best_row + r][best_col + c] for c in range(3)])