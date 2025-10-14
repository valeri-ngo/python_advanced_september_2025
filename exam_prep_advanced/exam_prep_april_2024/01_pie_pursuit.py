from collections import deque

contestants = deque(int(c) for c in input().split())
pies = [int(p) for p in input().split()]


while contestants and pies:

    contestant = contestants.popleft()
    pie = pies.pop()

    if contestant >= pie:
        contestant -= pie
        if contestant > 0:
            contestants.append(contestant)

    else:
        pie -= contestant

        if pie == 1:
            if pies:
                pies[-1] += 1
            else:
                pies.append(1)
        else:
            pies.append(pie)

if not pies and contestants:
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join(str(x) for x in contestants)}")
elif not pies and not contestants:
    print("We have a champion!")
elif not contestants and pies:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join(str(x) for x in pies)}")
