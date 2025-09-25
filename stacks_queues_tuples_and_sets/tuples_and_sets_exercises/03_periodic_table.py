num = int(input())
chemical_set = set()

for _ in range(num):
    chemical_compounds = input().split()
    for char in chemical_compounds:
        chemical_set.add(char)

print(*chemical_set, sep='\n')