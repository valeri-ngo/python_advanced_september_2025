rows = int(input())
matrix = []
player_position = [0, 0]
collected_stars = 2


moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(rows):
    line = input().split()
    matrix.append(line)
    for col in range(len(line)):
        if line[col] == "P":
            player_position = [row, col]

first_move = True

while collected_stars < 10:
    command = input()

    if command in moves:
        new_row = player_position[0] + moves[command][0]
        new_col = player_position[1] + moves[command][1]

        if first_move:
            r0, c0 = player_position
            matrix[r0][c0] = "."
            first_move = False

        if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
            target_row, target_col = new_row, new_col
        else:
            target_row, target_col = 0, 0

        cell = matrix[target_row][target_col]
        if cell == "#":
            collected_stars -= 1
            if collected_stars <= 0:
                print("Game over! You are out of any stars.")
                break
        elif cell == "*":
            collected_stars += 1
            matrix[target_row][target_col] = "."
            player_position = [target_row, target_col]
        else:
            player_position = [target_row, target_col]

    if collected_stars >= 10:
        print(f"You won! You have collected {collected_stars} stars.")
        break

r, c = player_position
matrix[r][c] = "P"
print(f"Your final position is [{r}, {c}]")
for row in matrix:
    print(" ".join(row))
