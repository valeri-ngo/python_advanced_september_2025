def draw_cards(*monster_cards, **spell_cards):

    monsters = {}
    spells = {}

    for name, card_type in monster_cards:
        if card_type == "monster":
            monsters[name] = card_type
        elif card_type == "spell":
            spells[name] = card_type

    for name, card_type in spell_cards.items():
        if card_type == "monster":
            monsters[name] = card_type
        elif card_type == "spell":
            spells[name] = card_type

    sorted_monsters = sorted(monsters.keys(), reverse=True)
    sorted_spells = sorted(spells.keys())

    result = ""

    if sorted_monsters:
        result += "Monster cards:\n"
        result += "".join(f"  ***{name}\n" for name in sorted_monsters)
    if sorted_spells:
        result += "Spell cards:\n"
        result += "".join(f"  $$${name}\n" for name in sorted_spells)

    return result.strip()

print(draw_cards(("cyber dragon", "monster"), freeze="spell",))
print()
print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))
print()
print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))
