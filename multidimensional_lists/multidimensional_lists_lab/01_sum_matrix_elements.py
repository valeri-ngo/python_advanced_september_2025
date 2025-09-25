row, col = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(row):
    row_data = [int(x) for x in input().split(", ")]
    matrix.append(row_data)

sum_lst = sum(sum(row) for row in matrix)
print(sum_lst)
print(matrix)
