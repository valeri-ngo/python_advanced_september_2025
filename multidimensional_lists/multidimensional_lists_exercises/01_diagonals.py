matrix = [[int(x) for x in input().split(", ")] for _ in range(int(input()))]

diagonal_sum = 0
opposite_diagonal = 0
diagonal_lst = []
opposite_diagonal_lst = []

for row_index in range(len(matrix)):
    diagonal_sum += matrix[row_index][row_index]
    diagonal_lst.append(matrix[row_index][row_index])
    opposite_diagonal += matrix[row_index][-row_index - 1]
    opposite_diagonal_lst.append(matrix[row_index][-row_index - 1])

print(f"Primary diagonal: {', '.join(map(str, diagonal_lst))}. Sum: {diagonal_sum}")
print(f"Secondary diagonal: {', '.join(map(str, opposite_diagonal_lst))}. Sum: {opposite_diagonal}")
