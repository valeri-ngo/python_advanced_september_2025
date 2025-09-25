num_commands = int(input())

car_counter = set()

for _ in range(num_commands):
    command = input().split(", ")
    direction = command[0]
    car = command[1]

    if direction == "IN":
        if not car in car_counter:
            car_counter.add(car)

    elif direction == "OUT":
        if car in car_counter:
            car_counter.remove(car)

if not car_counter:
    print(f"Parking Lot is Empty")
else:
    for car in car_counter:
        print(car, sep='\n')