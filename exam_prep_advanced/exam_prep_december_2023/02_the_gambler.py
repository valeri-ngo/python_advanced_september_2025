rows = int(input())
matrix = [list(input().strip()) for _ in range(rows)]
gambler_pos = (0, 0)
money = 100

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(rows):
    for col in range(len(matrix[row])):
        if matrix[row][col] == "G":
            gambler_pos = (row, col)
        else:
            continue
        break

while True:
    command = input().strip().lower()

    if command == "end":
        print(f"End of the game. Total amount: {money}$")
        for row in matrix:
            print("".join(row))
        break

    if command not in moves:
        continue

    elif command in moves:
        dr, dc = moves[command]
        player_row, player_col = gambler_pos
        new_row, new_col = player_row + dr, player_col + dc

        if not (0 <= new_row < rows and 0 <= new_col < len(matrix[new_row])):
            money = 0
            print("Game over! You lost everything!")
            break

        cell = matrix[new_row][new_col]

        if cell == "W":
            money += 100
            matrix[player_row][player_col] = "-"
            matrix[new_row][new_col] = "G"
            gambler_pos = (new_row, new_col)

        elif cell == "P":
            money -= 200
            if money <= 0:
                money = 0
                print("Game over! You lost everything!")
                break

            matrix[player_row][player_col] = '-'
            matrix[new_row][new_col] = "G"
            gambler_pos = (new_row, new_col)

        elif cell == "J":
            money += 100000
            matrix[player_row][player_col] = "-"
            matrix[new_row][new_col] = "G"
            gambler_pos = (new_row, new_col)
            print(f"You win the Jackpot!\nEnd of the game. Total amount: {money}$")

            for row in matrix:
                print("".join(row))

            break

        elif cell == "-":
            matrix[player_row][player_col] = "-"
            matrix[new_row][new_col] = "G"
            gambler_pos = (new_row, new_col)
