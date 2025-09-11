from collections import deque

price_per_bullet = int(input())
barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())
value_price = int(input())
shots = 0

while locks and bullets:
    shots += 1
    curr_bullet = bullets.pop()
    value_price -= price_per_bullet

    if locks[0] >= curr_bullet:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")

    if shots == barrel_size and bullets:
        shots = 0
        print("Reloading!")

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${value_price}")