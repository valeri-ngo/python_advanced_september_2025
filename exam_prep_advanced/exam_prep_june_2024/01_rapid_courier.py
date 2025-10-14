from collections import deque

packages = [int(p) for p in input().split()]
couriers = deque([int(c) for c in input().split()])

total_weight_delivered = 0

while packages and couriers:

    package = packages[-1]
    courier = couriers.popleft()

    if courier >= package:
        total_weight_delivered += package
        packages.pop()

        courier -= 2 * package
        if courier > 0:
            couriers.append(courier)

    else:
        total_weight_delivered += courier
        packages[-1] -= courier

print(f"Total weight: {total_weight_delivered} kg")

if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif packages and not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(map(str, packages))}")
elif couriers and not packages:
    print(f"Couriers are still on duty: {', '.join(map(str, couriers))} but there are no more packages to deliver.")