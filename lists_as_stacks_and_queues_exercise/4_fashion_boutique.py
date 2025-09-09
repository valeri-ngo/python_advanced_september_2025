clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

racks = 0

while clothes:
    racks += 1
    curr_rack_capacity = rack_capacity
    while clothes and clothes[-1] <= curr_rack_capacity:
        curr_rack_capacity -= clothes.pop()

print(racks)
