square = int(input())

matrix = []

for _ in range(square):
    row = [int(x) for x in input().split()]
    matrix.append(row)

bombs = input().split()
bombs = [b.split(",") for b in bombs]
bombs = [(int(r), int(c)) for r, c in bombs]

directions = [
    (-1, -1), (-1 , 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]
for br, bc in bombs:
    power = matrix[br][bc]
    if power <= 0:
        continue

    matrix[br][bc] = 0

    for dr, dc in directions:
        nr, nc = br + dr, bc + dc
        if 0 <= nr < square and 0 <= nc < square:
            if matrix[nr][nc] > 0:
                matrix[nr][nc] -= power

alive_cells = 0
alive_sum = 0

for r in range(square):
    for c in range(square):
        if matrix[r][c] > 0:
            alive_cells += 1
            alive_sum += matrix[r][c]

print(f"Alive cells: {alive_cells}")
print(f"Sum: {alive_sum}")

for row in matrix:
    print(*row)