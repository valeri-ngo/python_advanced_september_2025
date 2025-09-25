presents = int(input())
n = int(input())

matrix = []
santa = []
nice_kids = 0
nice_kids_gifted = 0

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "S":
            santa = [row, col]
        elif matrix[row][col] == "V":
            nice_kids += 1

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, +1)
    }

while presents > 0:
    command = input()
    if command == "Christmas morning":
        break
    r = santa[0] + moves[command][0]
    c = santa[1] + moves[command][1]

    if 0 <= r < n and 0 <= c < n:
        if matrix[r][c] == "V":
            presents -= 1
            nice_kids_gifted += 1
            matrix[r][c] = "-"
        elif matrix[r][c] == "C":
            for direction in moves.values():
                next_row, next_col = r + direction[0], c + direction[1]
                if matrix[next_row][next_col] in "VX" and presents > 0:
                    presents -= 1
                    if matrix[next_row][next_col] == "V":
                        nice_kids_gifted += 1
                    matrix[next_row][next_col] = "-"
        matrix[santa[0]][santa[1]] = "-"
        santa = [r, c]
        matrix[r][c] = "S"

if presents < 1 and nice_kids - nice_kids_gifted > 0:
    print(f"Santa ran out of presents!")
[print(*row) for row in matrix]
if nice_kids - nice_kids_gifted > 0:
    print(f"No presents for {nice_kids - nice_kids_gifted} nice kid/s.")
else:
    print(f"Good job, Santa! {nice_kids_gifted} happy nice kid/s.")