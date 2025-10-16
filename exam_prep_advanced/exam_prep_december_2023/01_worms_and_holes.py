from collections import deque

worms = [int(w) for w in input().split()]
holes = deque(int(h) for h in input().split())
matched = 0
initial_worms = len(worms)

while worms and holes:

    current_worm = worms[-1]
    if current_worm <=0:
        worms.pop()
        continue

    current_hole = holes[0]

    if current_worm == current_hole:
        worms.pop()
        holes.popleft()
        matched += 1
    else:
        holes.popleft()
        worms[-1] -= 3
        if worms[-1] <= 0:
            worms.pop()

if matched > 0:
    print(f"Matches: {matched}")
else:
    print("There are no matches.")

if not worms:
    if matched == initial_worms:
        print("Every worm found a suitable hole!")
    else:
        print("Worms left: none")
else:
    print(f"Worms left: {', '.join(map(str, worms))}")

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(map(str, holes))}")
