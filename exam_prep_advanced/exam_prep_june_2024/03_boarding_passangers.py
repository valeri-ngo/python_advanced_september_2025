def boarding_passengers(capacity, *passengers):
    boarded = {}
    total_boarded = 0

    for number, plan in passengers:
        if capacity == 0:
            break
        if number <= capacity:
            boarded[plan] = boarded.get(plan, 0) + number
            capacity -= number
            total_boarded += number

    sorted_boarded = sorted(boarded.items(), key=lambda kvp: (-kvp[1], kvp[0]))
    result = ["Boarding details by benefit plan:"]
    for plan, guests in sorted_boarded:
        result.append(f"## {plan}: {guests} guests")

    if total_boarded == sum(num for num, _ in passengers):
        result.append("All passengers are successfully boarded!")
    elif capacity == 0 and total_boarded < sum(num for num, _ in passengers):
        result.append("Boarding unsuccessful. Cruise ship at full capacity.")
    else:
        result.append(f"Partial boarding completed. Available capacity: {capacity}.")

    return "\n".join(result)

print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
print()
print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))
print()
print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))
