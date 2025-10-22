from collections import deque

substance_quantities = [int(s) for s in input().split(", ")]
crystal_energy = deque([int(c) for c in input().split(", ")])
created_potions = 0
crafted_potions = []
crafted_potions_names = set()

potions = {
    110: "Brew of Immortality",
    100: "Essence of Resilience",
    90: "Draught of Wisdom",
    80: "Potion of Agility",
    70: "Elixir of Strength",
}

sorted_potions = sorted(potions.items(), reverse= True)

while crystal_energy and substance_quantities and created_potions < 5:
    current_substance = substance_quantities.pop()
    current_crystal = crystal_energy.popleft()

    sum_mats = current_crystal + current_substance

    if sum_mats in potions and potions[sum_mats] not in crafted_potions_names:
        crafted_potions.append(potions[sum_mats])
        crafted_potions_names.add(potions[sum_mats])
        created_potions += 1

    else:
        target_energy = None

        for energy, name in sorted_potions:
            if energy <= sum_mats and name not in crafted_potions_names:
                target_energy = energy
                break

        if target_energy is not None:
            crafted_potions.append(potions[target_energy])
            crafted_potions_names.add(potions[target_energy])
            created_potions += 1

            reduced = current_crystal - 20

            if reduced > 0:
                crystal_energy.append(reduced)

        else:
            reduced = current_crystal - 5
            if reduced > 0:
                crystal_energy.append(reduced)

if created_potions == 5:
    print("Success! The alchemist has forged all potions!")
else:
    print("The alchemist failed to complete his quest.")

if crafted_potions:
    print(f"Crafted potions: " + ", ".join(crafted_potions))

if substance_quantities:
    print(f"Substances: " + ", ".join(map(str, substance_quantities[::-1])))
if crystal_energy:
    print(f"Crystals: " + ", ".join(map(str, crystal_energy)))