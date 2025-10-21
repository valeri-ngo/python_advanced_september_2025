def choose_coins(coins, targets):
    coins.sort(reverse= True)
    used_coins = {}

    index = 0
    while targets != 0 and index < len(coins):
        count_coins = targets // coins[index]
        targets %= coins[index]

        if count_coins > 0:
            used_coins[coins[index]] = count_coins
        index += 1

    if targets != 0:
        return "Error"

    result = f"Number of coins to take: {sum(used_coins.values())}\n"
    for value, count in used_coins.items():
        result += f"{count} coin(s) with value {value}\n"

    return result.strip()

coins_list = [int(c) for c in input().split(", ")]
target = int(input())
print(choose_coins(coins_list, target))