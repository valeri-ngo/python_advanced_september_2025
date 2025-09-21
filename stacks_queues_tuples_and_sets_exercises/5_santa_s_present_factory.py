from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque(int(x) for x in input().split())

presents = {}

points = {
    150 : "Doll",
    250 : "Wooden train",
    300 : "Teddy bear",
    400 : "Bicycle"
}

while materials and magic_level:
    total_magic = materials[-1] * magic_level[0]
    if total_magic in points:
        new_present = points[total_magic]
        if new_present not in presents:
            presents[new_present] = 0
        presents[new_present] += 1
        materials.pop()
        magic_level.popleft()
    elif total_magic < 0:
        materials.append(materials.pop() + magic_level.popleft())
    elif total_magic > 0:
        magic_level.popleft()
        materials[-1] += 15
    else:
        if materials[-1] == 0:
            materials.pop()
        if magic_level[0] == 0:
            magic_level.popleft()

if ("Doll" in presents and "Wooden train" in presents) or (
        "Teddy bear" in presents and "Bicycle" in presents):
    print(f"The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

for key, value in sorted(presents.items()):
    if value > 0:
        print(f"{key}: {value}")
