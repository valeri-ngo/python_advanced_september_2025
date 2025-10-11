def triangle(num):
    result = ""

    for row in range(1, num + 1):
        for col in range(1, row +1, +1):
            result += f"{col}"+ " "
        result += "\n"

    for row in range(num -1, 0, -1):
        for col in range(1, row +1):
            result += f"{col}"+ " "
        result += "\n"
    return result