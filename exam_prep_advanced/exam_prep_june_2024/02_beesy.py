rows = int(input())
matrix = [[x for x in input()] for _ in range(rows)]
cols = len(matrix[0])

bee_position = []
initial_energy = 15
nectar = 0
restored = False

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(rows):
    for col in range(len(matrix[row])):
        if matrix[row][col] == "B":
            bee_position = [row, col]

while True:
    directions = input()
    if directions not in moves:
        continue

    initial_energy -= 1

    nr, nc = moves[directions]
    new_row = (bee_position[0] + nr) % rows
    new_col = (bee_position[1] + nc) % cols

    cell = matrix[new_row][new_col]

    if cell.isdigit():
        nectar += int(cell)
        matrix[new_row][new_col] = "-"
    elif cell == "H":
        old_r, old_c = bee_position
        matrix[old_r][old_c] = "-"
        bee_position = [new_row, new_col]
        matrix[new_row][new_col] = "B"
        if nectar >= 30:
            print(f"Great job, Beesy! The hive is full. Energy left: {initial_energy}")
            break
        else:
            print(f"Beesy did not manage to collect enough nectar.")
            break

    old_r, old_c = bee_position
    matrix[old_r][old_c] = "-"
    bee_position = [new_row, new_col]
    matrix[new_row][new_col] = "B"

    if initial_energy <= 0:
        if not restored and nectar >= 30:
            initial_energy += nectar - 30
            nectar = 30
            restored = True

            if initial_energy <= 0:
                print(f"This is the end! Beesy ran out of energy.")
                break
        else:
            print(f"This is the end! Beesy ran out of energy.")
            break

for row in matrix:
    print("".join(row))
