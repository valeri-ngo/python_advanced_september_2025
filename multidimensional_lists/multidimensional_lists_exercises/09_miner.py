square = int(input())

commands = input().split()
directions = {
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1),
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c:(r + 1 , c)
}

matrix = [input().split() for _ in range(square)]

for row in range(square):
    for col in range(square):
        if matrix[row][col] == "s":
            start_r, start_c = row, col
            matrix[row][col] = "*"

total_coal = sum(row.count("c") for row in matrix)
collected = 0
miner_r, miner_c = start_r, start_c

for comm in commands:
    nr, nc = directions[comm](miner_r, miner_c)
    if not (0 <= nr < square and 0 <= nc < square):
        continue
    miner_r, miner_c = nr, nc

    cell = matrix[miner_r][miner_c]
    if cell == "e":
        print(f"Game over! ({miner_r}, {miner_c})")
        break
    elif cell == "c":
        collected += 1
        matrix[miner_r][miner_c] = "*"
        if collected == total_coal:
            print(f"You collected all coal! ({miner_r}, {miner_c})")
            break
else:
    remaining = total_coal - collected
    print(f"{remaining} pieces of coal left. ({miner_r}, {miner_c})")
