from collections import deque

green_light_time = int(input())
free_window_time = int(input())
cars = deque()
cars_passed = 0
crashed = False

while True:

    command = input()

    if command == 'END':
        break
    elif command != 'green':
        cars.append(command)

    elif command == 'green':
        time_left = green_light_time

        while cars and time_left > 0:
            car = cars.popleft()
            car_len = len(car)

            if car_len <= time_left:
                cars_passed += 1
                time_left -= car_len
            else:
                remaining = car_len - time_left

                if remaining <= free_window_time:
                    cars_passed += 1
                    time_left = 0
                else:
                    hit_index = time_left + free_window_time
                    print(f"A crash happened!")
                    print(f"{car} was hit at {car[hit_index]}.")
                    crashed = True
                    break
    if crashed:
        break

if not crashed:
    print(f"Everyone is safe.")
    print(f"{cars_passed} total cars passed the crossroads.")