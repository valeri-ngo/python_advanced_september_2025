n = int(input())

matrix = [[x for x in input().split()] for _ in range(n)]
alice_pos = []

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, +1)
    }

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == "A":
            matrix[row][col] = "*"
            alice_pos = [row, col]

tea_bags = 0

while tea_bags < 10:

    direction = input()
    move = moves[direction]
    r = alice_pos[0] + move[0]
    c = alice_pos[1] + move[1]

    if r < 0 or r >= n or c < 0 or c >= n:
        break

    if matrix[r][c] == "R":
        matrix[r][c] = "*"
        break

    if matrix[r][c] not in "*.":
        tea_bags += int(matrix[r][c])

    matrix[r][c] = "*"
    alice_pos = [r, c]

if tea_bags >= 10:
    print(f"She did it! She went to the party.")
else:
    print(f"Alice didn't make it to the tea party.")

[print(*row) for row in matrix]