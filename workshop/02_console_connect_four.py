class InvalidColumnError(Exception):
    pass


class FullColumnError(Exception):
    pass


SLOTS_TO_WIN = 4



def create_matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]


def validate_column_choice(column, max_index):
    if not (0 <= column <= max_index):
        raise InvalidColumnError


def place_player_choice(ma, c, player_n):
    for r in range(len(ma) - 1, -1, -1):
        if ma[r][c] == 0:
            ma[r][c] = player_n
            return r, c
    raise FullColumnError


def print_matrix(ma):
    for line in ma:
        print(line)


def is_player_num(ma, r, c, player_n):
    try:
        return ma[r][c] == player_n
    except IndexError:
        return False


def is_vertical_win(ma, r, c, player_n, slots):
    return all(is_player_num(ma, r + idx, c, player_n) for idx in range(slots))


def is_horizontal_win(ma, r, c, player_n, slots):
    filled = 1

    for idx in range(1, slots):
        if is_player_num(ma, r, c + idx, player_n):
            filled += 1
        else:
            break

    for idx in range(1, slots):
        if is_player_num(ma, r, c - idx, player_n):
            filled += 1
        else:
            break

    return filled >= slots



def is_right_diagonal_win(ma, r, c, player_n, slots):
    filled = 1

    for idx in range(1, slots):
        if is_player_num(ma, r - idx, c + idx, player_n):
            filled += 1
        else:
            break

    for idx in range(1, slots):
        if is_player_num(ma, r + idx, c - idx, player_n):
            filled += 1
        else:
            break

    return filled >= slots


def is_left_diagonal_win(ma, r, c, player_n, slots):
    filled = 1

    for idx in range(1, slots):
        if is_player_num(ma, r + idx, c + idx, player_n):
            filled += 1
        else:
            break

    for idx in range(1, slots):
        if is_player_num(ma, r - idx, c - idx, player_n):
            filled += 1
        else:
            break

    return filled >= slots


def is_winner(ma, r, c, player_n, slots=SLOTS_TO_WIN):
    return any([
        is_vertical_win(ma, r, c, player_n, slots),
        is_horizontal_win(ma, r, c, player_n, slots),
        is_right_diagonal_win(ma, r, c, player_n, slots),
        is_left_diagonal_win(ma, r, c, player_n, slots)
    ])

rows_count = 6
cols_count = 7

matrix = create_matrix(rows_count, cols_count)

player_num = 1
counter = 0

while True:
    player_num = 2 if player_num % 2 == 0 else 1
    try:
        column_num = int(input(f"Player {player_num}, please choose a column: ")) - 1
        validate_column_choice(column_num, cols_count - 1)
        row, col = place_player_choice(matrix, column_num, player_num)
        print_matrix(matrix)
        if is_winner(matrix, row, col, player_num):
            print(f"The winner is Player # {player_num}!")
            break
    except InvalidColumnError:
        print(f"Out of range. Please choose a number between 1 - {cols_count} : ")
    except FullColumnError:
        print(f"The column is full. Please select another column number: ")
    except ValueError:
        print("Please enter a valid number.")

    counter += 1
    if counter == rows_count * cols_count:
        print("Draw! No one wins.")
        break

    player_num += 1