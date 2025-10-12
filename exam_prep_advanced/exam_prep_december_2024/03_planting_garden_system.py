def plant_garden(available_space, *args, **kwargs):
    planted = {}
    allowed_plants = {}
    result = ""

    for plant_type, space_per_piece in args:
        allowed_plants[plant_type] = space_per_piece

    sorted_requests = sorted(kwargs.items(), key= lambda kvp: kvp[0])

    for plant_name, quantity in sorted_requests:
        if plant_name not in allowed_plants:
            continue
        space_per_piece = allowed_plants[plant_name]
        max_planted = int(available_space // space_per_piece)
        planted_piece = min(quantity, max_planted)

        if planted_piece > 0:
            planted[plant_name] = planted_piece
            available_space -= planted_piece * space_per_piece

        if available_space <= 0:
            break

    all_fully_planted = True
    for plant_name, requested_pieces in kwargs.items():
        if plant_name not in allowed_plants:
            continue
        if planted.get(plant_name, 0) != requested_pieces:
            all_fully_planted = False
            break

    if all_fully_planted:
        result += f"All plants were planted! Available garden space: {available_space:.1f} sq meters.\n"
    else:
        result += f"Not enough space to plant all requested plants!\n"
    result += "Planted plants:"
    for plant_type in sorted(planted):
        result += f"\n{plant_type}: {planted[plant_type]}"
    return result

print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))
print()
print(plant_garden(20.0, ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, sunflower=5))
print()
print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))
print()
print(plant_garden(50.0, ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, daisy=1))