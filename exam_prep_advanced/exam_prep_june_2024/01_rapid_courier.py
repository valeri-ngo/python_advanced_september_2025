from collections import deque

package_weight = [int(x) for x in input().split()]
available_courier = deque(int(x) for x in input().split())
total_delivered_weight = 0

while package_weight and available_courier:

    current_package = package_weight[-1]
    current_courier = available_courier[0]

    if current_courier > current_package:
        current_courier -= current_package * 2
        package_weight.pop()
        total_delivered_weight += current_package

        if current_courier > 0:
            available_courier[0] = current_courier
            available_courier.rotate(-1)
        else:
            available_courier.popleft()

    elif current_courier < current_package:
        package_weight[-1] -= current_courier
        available_courier.popleft()
        total_delivered_weight += current_courier

    else:
        package_weight.pop()
        available_courier.popleft()
        total_delivered_weight += current_package

print(f"Total weight: {total_delivered_weight} kg")

if not package_weight:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
    if available_courier:
        print("Couriers left with capacity: " + ", ".join(map(str, available_courier)))
elif not available_courier:
    print("Unfortunately, there are no more available couriers to deliver the following packages: "
          + ", ".join(map(str, package_weight)))
else:
    print("Couriers left with capacity: " + ", ".join(map(str, available_courier)))
