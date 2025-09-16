num = int(input())

set_names = set()

for _ in range(num):
    name = input()

    if not name in set_names:
        set_names.add(name)

for names in set_names:
    print(names, sep='\n')