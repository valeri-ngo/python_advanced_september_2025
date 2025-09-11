from collections import deque

cup_capacity = deque(int(x) for x in input().split())
bottle_capacity = [int(x) for x in input().split()]
water_left = 0

while cup_capacity and bottle_capacity:

    curr_bottle = bottle_capacity.pop()

    if curr_bottle >= cup_capacity[0]:
        water_left += curr_bottle - cup_capacity[0]
        cup_capacity.popleft()
    else:
        cup_capacity[0] -= curr_bottle

if cup_capacity:
    print(f"Cups: {' '.join(map(str, cup_capacity))}")
else:
    print(f"Bottles: {' '.join(map(str, reversed(bottle_capacity)))}")

print(f"Wasted litters of water: {water_left}")