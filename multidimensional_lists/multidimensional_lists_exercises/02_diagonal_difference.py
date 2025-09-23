row = int(input())

matrix = []

for _ in range(row):
    row_data = [int(x) for x in input().split()]
    matrix.append(row_data)

diagonal_sum = 0
secondary_diagonal = 0

for row_index in range(row):
    diagonal_sum += matrix[row_index][row_index]
    secondary_diagonal += matrix[row_index][-row_index - 1]

print(abs(diagonal_sum - secondary_diagonal))
