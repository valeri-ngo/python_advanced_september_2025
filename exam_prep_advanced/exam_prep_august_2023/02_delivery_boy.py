rows, cols = [int(x) for x in input().split()]

matrix = []
delivery_pos = (0, 0)
has_pizza = False

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(rows):
    line = list(input().strip())
    matrix.append(line)
    for col in range(cols):
        if matrix[row][col] == "B":
            delivery_pos = (row, col)

while True:

    command = input().strip().lower()

    if command not in moves:
        continue

    dr, dc = moves[command]
    d_row, d_col = delivery_pos
    new_r, new_c = d_row + dr, d_col + dc

    if not (0 <= new_r < rows and 0 <= new_c < cols):
        print("The delivery is late. Order is canceled.")
        matrix[d_row][d_col] = ' '
        break

    cell = matrix[new_r][new_c]

    if cell == "*":
        continue

    matrix[d_row][d_col] = '.'

    if cell == "P":
        has_pizza = True
        matrix[new_r][new_c] = 'R'
        print("Pizza is collected. 10 minutes for delivery.")

    elif cell == "A" and has_pizza:
        matrix[new_r][new_c] = "P"
        print("Pizza is delivered on time! Next order...")
        delivery_pos = (new_r, new_c)
        break

    else:
        delivery_pos = (new_r, new_c)

d_row, d_col = delivery_pos
if matrix[d_row][d_col] not in ['P', 'R']:
    matrix[d_row][d_col] = 'B'

for row in matrix:
    print(''.join(row))