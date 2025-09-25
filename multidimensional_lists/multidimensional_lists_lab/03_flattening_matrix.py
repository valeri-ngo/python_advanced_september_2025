rows = int(input())

matrix = []

for _ in range(rows):
    cols = [int(x) for x in input().split(", ")]
    matrix.extend(cols)
print(matrix)
