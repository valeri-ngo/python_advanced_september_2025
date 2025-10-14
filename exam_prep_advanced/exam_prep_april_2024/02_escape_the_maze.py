rows = int(input())

matrix = [list(input().strip()) for _ in range(rows)]
player_position = (0, 0)
health = 100
escaped = False

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(rows):
    for col in range(len(matrix[row])):
        if matrix[row][col] == "P":
            player_position = (row, col)

while True:
    command = input().strip().lower()

    if command not in moves:
        break

    new_row = player_position[0] + moves[command][0]
    new_col = player_position[1] + moves[command][1]

    if not (0 <= new_row < rows and 0 <= new_col < len(matrix[new_row])):
        continue

    cell = matrix[new_row][new_col]
    prev_r, prev_c = player_position

    if cell == "X":
        matrix[prev_r][prev_c] = "-"
        matrix[new_row][new_col] = "P"
        print("Player escaped the maze. Danger passed!")
        escaped = True
        break

    if cell == "M":
        health -= 40
        matrix[prev_r][prev_c] = "-"
        player_position = (new_row, new_col)
        matrix[new_row][new_col] = "P"
        if health <= 0:
            print("Player is dead. Maze over!")
            print(f"Player's health: 0 units")
            break

    elif cell == "H":
        health = min(100, health + 15)
        matrix[prev_r][prev_c] = "-"
        player_position = (new_row, new_col)
        matrix[new_row][new_col] = "P"

    else:
        matrix[prev_r][prev_c] = "-"
        player_position = (new_row, new_col)
        matrix[new_row][new_col] = "P"

if escaped:
    print(f"Player's health: {health} units")
for row in matrix:
    print("".join(row))
