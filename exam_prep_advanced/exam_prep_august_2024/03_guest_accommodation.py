def accommodate(*guests, **rooms):

    def sort_key(item):
        room_n, capacity = item
        room_number = int(room_n.split("_")[1])
        return (capacity, room_number)

    sorted_rooms = sorted(rooms.items(), key=sort_key)

    available_rooms = []

    for room_name, capacity in sorted_rooms:
        room_num = int(room_name.split("_")[1])
        available_rooms.append((room_num,room_name, capacity))

    accommodations = []
    unaccommodated = 0

    for group in guests:
        picked = best_fit(available_rooms, group)
        if picked is None:
            unaccommodated += group
        else:
            room_num, room_name, cap = picked
            accommodations.append((room_num, group))

    accommodations.sort(key= lambda x: x[0])

    if accommodations:
        result = f"A total of {len(accommodations)} accommodations were completed!\n"
        for room_num, guests_count in accommodations:
            result += f"<Room {room_num} accommodates {guests_count} guests>\n"
    else:
        result = "No accommodations were completed!\n"

    if unaccommodated:
        result += f"Guests with no accommodation: {unaccommodated}\n"
    if available_rooms:
        result += f"Empty rooms: {len(available_rooms)}"

    return result.strip()


def best_fit(available_rooms, group_size):
    for index in range(len(available_rooms)):
        room_num, room_name, cap = available_rooms[index]
        if cap >= group_size:
            return available_rooms.pop(index)
    return None


print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print()
print(accommodate(10, 9, 8, room_307=6, room_802=5))
print()
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))