def team_lineup(*args):
    country_sort = {}

    for player_name, country_name in args:
        if country_name not in country_sort:
            country_sort[country_name] = []
        if player_name not in country_sort[country_name]:
            country_sort[country_name].append(player_name)
    sort_by_players = sorted(country_sort.items(), key= lambda kvp: (-len(kvp[-1]), kvp[0]))

    result = ""

    for country, players in sort_by_players:
        result += f"{country}:\n"
        for player in players:
            result += f"  -{player}\n"

    return  result

print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))
print()
print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))
print()
print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))
