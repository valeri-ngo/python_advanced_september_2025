rows = int(input())

matrix = [list(input().strip()) for _ in range(rows)]
pacman_pos = (0, 0)
health = 100
first_move = False
has_immune = False
stars = 0
cols = len(matrix[0])

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == 'P':
            pacman_pos = (row, col)
        elif matrix[row][col] == "*":
            stars += 1

while True:

    command = input()

    if command == "end":
        break

    if command not in moves:
        continue

    dr, dc = moves[command]
    r, c = pacman_pos

    if not first_move:
        matrix[r][c] = '-'
        first_move = True

    nr, nc = (r + dr) % rows, (c + dc) % cols

    cell = matrix[nr][nc]

    if cell == "*":
        stars -= 1
        matrix[nr][nc] = '-'
        pacman_pos = (nr, nc)

    elif cell == "G":
        if has_immune:
            has_immune = False
        else:
            health -= 50
        matrix[nr][nc] = '-'
        pacman_pos = (nr, nc)

    elif cell == "F":
        has_immune = True
        matrix[nr][nc] = '-'
        pacman_pos = (nr, nc)

    elif cell == "-":
        pacman_pos = (nr, nc)

    if stars == 0:
        break

    if health <= 0:
        break

prev_r, prev_c = pacman_pos
matrix[prev_r][prev_c] = 'P'

if health <= 0:
    print(f"Game over! Pacman last coordinates [{prev_r},{prev_c}]")
elif stars == 0:
    print(f"Pacman wins! All the stars are collected.")
else:
    print("Pacman failed to collect all the stars.")

print(f"Health: {health}")

if stars > 0:
    print(f"Uncollected stars: {stars}")

for row in matrix:
    print(''.join(row))