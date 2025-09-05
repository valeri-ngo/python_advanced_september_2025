from collections import deque

name = deque(input().split())
number_toss = int(input()) - 1
turns = 0

while len(name) > 1:
    name.rotate(-number_toss)
    print(f"Removed {name.popleft()}")

print(f"Last is {name.popleft()}")
