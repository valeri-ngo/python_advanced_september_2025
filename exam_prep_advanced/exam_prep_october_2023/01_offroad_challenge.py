from collections import deque

initial_fuel = input().split()
consumption = deque(input().split())
amount_of_fuel = deque(input().split())
altitude = 0
reached_altitude = []

while initial_fuel and amount_of_fuel and amount_of_fuel:
    altitude += 1
    current_fuel = int(initial_fuel[-1])
    current_consumption = int(consumption[0])
    needed_fuel = int(amount_of_fuel[0])
    sum_fuel = current_fuel - current_consumption

    if sum_fuel >= needed_fuel:
        reached_altitude.append(f"Altitude {altitude}")
        print(f"John has reached: Altitude {altitude}")
        initial_fuel.pop()
        consumption.popleft()
        amount_of_fuel.popleft()
    else:
        print(f"John did not reach: Altitude {altitude}")
        break

if len(reached_altitude) == 4:
    print("John has reached all the altitudes and managed to reach the top!")
elif len(reached_altitude) > 0:
    print("John failed to reach the top.")
    print(f"Reached altitudes: " + ", ".join(reached_altitude))
else:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")

