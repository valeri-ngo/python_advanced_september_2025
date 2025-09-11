from collections import deque

pumps_num = int(input())

pumps = deque()

for _ in range(pumps_num):
    curr_fuel, distance = input().split()
    pumps.append({'fuel': int(curr_fuel), 'distance': int(distance)})

starting_position = 0
stops = 0

while stops < pumps_num:
    fuel = 0

    for i in range(pumps_num):
        fuel += pumps[i]["fuel"]
        dist = pumps[i]["distance"]

        if fuel < dist:
            pumps.rotate(-1)
            starting_position += 1
            stops = 0
            break

        fuel -= dist
        stops += 1

print(starting_position)