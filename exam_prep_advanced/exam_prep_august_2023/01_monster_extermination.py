from collections import deque

monsters_deq = deque(int(x) for x in input().split(','))
soldiers_stack = [int(x) for x in input().split(',')]
monsters_defeated = 0

while monsters_deq and soldiers_stack:
    monster_armour = monsters_deq.popleft()
    soldiers_strike = soldiers_stack.pop()

    if soldiers_strike >= monster_armour:
        monsters_defeated += 1
        soldiers_strike -= monster_armour
        if soldiers_stack:
            soldiers_stack[-1] += soldiers_strike
        elif not soldiers_stack and soldiers_strike > 0:
            soldiers_stack.append(soldiers_strike)
    else:
        monster_armour -= soldiers_strike
        monsters_deq.append(monster_armour)

if not monsters_deq:
    print("All monsters have been killed!")
if not soldiers_stack:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {monsters_defeated}")
