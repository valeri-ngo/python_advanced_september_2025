def in_bounds(r, c, n):
    return 0 <= r < n and 0 <= c < n


def print_grid(grid):
    for row in grid:
        print(' '.join(row))

REFUEL = 10
PENALTY = 5
MAX_RES = 100
MOVE = 5

n = int(input())
matrix = [input().split() for _ in range(n)]

spaceship_location = None
for r in range(n):
    for c in range(n):
        if matrix[r][c] == "S":
            spaceship_location = (r, c)
            matrix[r][c] = '.'
            break
    if spaceship_location is not None:
        break


moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
    }

resources = MAX_RES


while True:
    try:
        directions = input()
    except EOFError:
        break

    if directions not in moves:
        continue

    dr, dc = moves[directions]

    nr = spaceship_location[0] + dr
    nc = spaceship_location[1] + dc

    if not in_bounds(nr, nc, n):
        print("Mission failed! The spaceship was lost in space.")
        r0, c0 = spaceship_location
        matrix[r0][c0] = 'S'
        print_grid(matrix)
        break

    spaceship_location = (nr, nc)
    resources -= MOVE
    cell = matrix[nr][nc]
    if cell == "M":
        resources -= PENALTY
        matrix[nr][nc] = '.'
    elif cell == "R":
        resources = min(MAX_RES, resources + REFUEL)
    elif cell == "P":
        print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left.")
        print_grid(matrix)
        break

    if resources < 5:
        print("Mission failed! The spaceship was stranded in space.")
        r0, c0 = spaceship_location
        matrix[r0][c0] = 'S'
        print_grid(matrix)
        break
