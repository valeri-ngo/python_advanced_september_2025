rows = int(input())

matrix = []
jet_pos = (0 , 0)
enemies = 0
armor = 300
result = ""

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for _ in range(rows):
    line = input().strip()
    row = line.split() if " " in line else list(line)
    matrix.append(row)

for row in range(rows):
    for col in range(len(matrix[row])):
        if matrix[row][col] == "J":
            jet_pos = (row, col)
        if matrix[row][col] == "E":
            enemies += 1

while True:
    commands = input().strip().lower()

    if commands not in moves:
        break

    dr, dc = moves[commands]

    new_r = jet_pos[0] + dr
    new_c = jet_pos[1] + dc

    if not (0 <= new_r < rows and 0 <= new_c < len(matrix[new_r])):
        continue

    prev_r, prev_c = jet_pos
    cell = matrix[new_r][new_c]

    if cell == "E":
        armor -= 100
        enemies -= 1
        matrix[prev_r][prev_c] = "-"
        jet_pos = (new_r, new_c)
        matrix[new_r][new_c] = "J"

        if armor <= 0:
            result = f"Mission failed, your jetfighter was shot down! Last coordinates [{new_r}, {new_c}]!"
            break

        if enemies == 0:
            result = "Mission accomplished, you neutralized the aerial threat!"
            break

    elif cell == "R":
        armor = min(300, armor + 300)
        matrix[prev_r][prev_c] = "-"
        jet_pos = (new_r, new_c)
        matrix[new_r][new_c] = "J"

    elif cell == "-":
        matrix[prev_r][prev_c] = "-"
        jet_pos = (new_r, new_c)
        matrix[new_r][new_c] = "J"

    else:
        continue

if result:
    print(result)

for row in matrix:
    print("".join(row))
