n = int(input())

matrix = [[x for x in input()] for _ in range(n)]
knights_pos = []

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == "K":
            knights_pos.append([row, col])

removed_knights = 0

moves = [(1, 2), (2, 1), (-1 , 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]

while True:
    max_hits = 0
    max_knight = [None, None]

    for k_row , k_col in knights_pos:
        hits = 0

        for move in moves:
            next_row = k_row + move[0]
            next_col = k_col + move[1]

            if 0 <= next_row < n and 0 <= next_col < n:
                if matrix[next_row][next_col] == "K":
                    hits += 1

        if hits > max_hits:
            max_hits = hits
            max_knight = [k_row, k_col]

    if max_hits == 0:
        break

    knights_pos.remove(max_knight)
    matrix[max_knight[0]][max_knight[1]] = "0"
    removed_knights += 1

print(removed_knights)
