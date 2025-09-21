num_guests = int(input())

numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
vip = set()
regular = set()
counter = 0

for _ in range(num_guests):
    reservation_code = input()

    if reservation_code.startswith(numbers):
        vip.add(reservation_code)
    else:
        regular.add(reservation_code)

while True:
    command = input()

    if command == 'END':
        break

    if command in vip:
        vip.remove(command)
    elif command in regular:
        regular.remove(command)

print(len(vip) + len(regular))

for guest in sorted(vip):
    print(guest, sep="\n")

for regular_guest in sorted(regular):
    print(regular_guest, sep='\n')