def cookbook(*recipes):
    from collections import defaultdict

    cuisines = defaultdict(list)
    for name, cuisine, ingredients in recipes:
        cuisines[cuisine].append((name, ingredients))

    sorted_cuisines = sorted(cuisines.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    result = []
    for cuisine, recipes_list in sorted_cuisines:
        recipes_list.sort(key=lambda kvp: kvp[0])
        result.append(f"{cuisine} cuisine contains {len(recipes_list)} recipes:")

        for name, ingredients in recipes_list:
            result.append(f"  * {name} -> Ingredients: {', '.join(ingredients)}")
    return "\n".join(result)

print(cookbook(
        ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
        ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
        ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
        ("Croissant", "French", ["flour", "butter", "yeast"]),
        ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
    ))
print()
print(cookbook(
    ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
    ))
print()
print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))