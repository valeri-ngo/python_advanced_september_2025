from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

honey_made = 0

operators = {
    "+" : lambda a, b : a + b,
    "-" : lambda a, b : a - b,
    "*" : lambda a, b : a * b,
    "/" : lambda a, b : a / b if b != 0 else 0
}

while working_bees and nectar:
    if nectar[-1] >= working_bees[0]:
        honey_made += abs(operators[symbols[0]](working_bees[0], nectar[-1]))
        nectar.pop()
        working_bees.popleft()
        symbols.popleft()
    else:
        nectar.pop()

print(f"Total honey made: {honey_made}")

if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")