row = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(row)]

command_dict = {
    "Add": lambda current, value: current + value,
    "Subtract": lambda current, value: current - value
}

while True:
    parts = input().split()
    if parts[0] == "END":
        break
    else:
        action = parts[0]
        r, c, value = map(int, parts[1:])

    if 0 <= r < row and 0 <= c < row:
        matrix[r][c] = command_dict[action](matrix[r][c], value)
    else:
        print("Invalid coordinates")

for r in matrix:
    print(*r)