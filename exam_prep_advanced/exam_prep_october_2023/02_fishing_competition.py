rows = int(input())
matrix = [list(input().strip()) for _ in range(rows)]
cols = len(matrix[0])
ship_pos = (0, 0)
fishes_caught = 0
whirlpool = False

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(rows):
    for col in range(len(matrix[row])):
        if matrix[row][col] == "S":
            ship_pos = (row, col)
            break
    else:
        continue
    break

while True:
    command = input().strip().lower()

    if command == "collect the nets":
        break

    if command not in moves:
        continue
    dr, dc = moves[command]
    s_row, s_col = ship_pos
    new_r = (s_row + dr) % rows
    new_c = (s_col + dc) % cols
    cell = matrix[new_r][new_c]
    if cell == "W":
        fishes_caught = 0
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the "
              f"ship: [{new_r},{new_c}]")
        whirlpool = True
        break
    if cell.isdigit():
        fishes_caught += int(cell)
    matrix[s_row][s_col] = "-"
    matrix[new_r][new_c] = "S"
    ship_pos = (new_r, new_c)

if not whirlpool:
    if fishes_caught >= 20:
        print("Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - fishes_caught} tons of fish more.")

    if fishes_caught > 0:
        print(f"Amount of fish caught: {fishes_caught} tons.")

    for row in matrix:
        print("".join(row))