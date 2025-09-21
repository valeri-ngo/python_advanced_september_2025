from collections import deque

chocolates = [int(x) for x in input().split(", ")]
cups_of_milk = deque(int(x) for x in input().split(", "))

milkshakes = 0

while chocolates and cups_of_milk and milkshakes < 5:
    if chocolates[-1] <= 0 and cups_of_milk[0] <= 0:
        chocolates.pop()
        cups_of_milk.popleft()
        continue
    if chocolates[-1] <= 0:
        chocolates.pop()
        continue
    if cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        continue

    if chocolates[-1] == cups_of_milk[0]:
        chocolates.pop()
        cups_of_milk.popleft()
        milkshakes += 1
    else:
        cups_of_milk.rotate(-1)
        chocolates[-1] -= 5

if milkshakes == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print(f"Not enough milkshakes.")
print(f"Chocolate: {', '.join(str(x) for x in chocolates) if chocolates else 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cups_of_milk) if cups_of_milk else 'empty'}")
