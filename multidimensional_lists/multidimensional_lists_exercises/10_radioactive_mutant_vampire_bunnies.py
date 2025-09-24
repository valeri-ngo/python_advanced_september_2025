def bunny_multiply(mat, bunnies_set):
    new_bunnies_set = set()
    directions = [(-1, 0),(1, 0),(0, - 1 ), (0, 1)]

    for b_row, b_col in bunnies_set:
        for d_row, d_col in directions:
            new_row, new_col = b_row + d_row, b_col + d_col
            if 0 <= new_row < len(mat) and 0 <= new_col < len(mat[0]):
                mat[new_row][new_col] = "B"
                new_bunnies_set.add((new_row, new_col))
    return mat, bunnies_set.union(new_bunnies_set)

rows, cols = [int(x) for x in input().split()]

matrix = []
player_r , player_c = None, None
bunnies = set()

for row in range(rows):
    matrix.append(list(input()))

    for col in range(cols):
        if matrix[row][col] == "P":
            player_r, player_c = row, col

        elif matrix[row][col] == "B":
            bunnies.add((row, col))

commands = list(input())

has_won = False
has_lost = False

moves = {
    "L": lambda r,c: (r, c - 1 ),
    "R": lambda r, c: (r, c + 1),
    "U": lambda r, c: (r - 1, c ),
    "D": lambda r, c: (r + 1, c)
}

for command in commands:
    new_player_r, new_player_c = moves[command](player_r, player_c)
    matrix, bunnies = bunny_multiply(matrix, bunnies)
    if (player_r, player_c) not in bunnies:
        matrix[player_r][player_c] = "."

    if new_player_r < 0 or new_player_r >= rows or \
            new_player_c < 0 or new_player_c >= cols:
        has_won = True
        break

    player_r, player_c = new_player_r, new_player_c
    if matrix[player_r][player_c] == "B":
        has_lost = True
        break

for row in matrix:
    print(''.join(row))

if has_won:
    print(f"won: {player_r} {player_c}")
elif has_lost:
    print(f"dead: {player_r} {player_c}")