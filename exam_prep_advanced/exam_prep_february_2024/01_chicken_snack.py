from collections import deque

amount_of_money = [int(m) for m in input().split()]
food_prices = deque([int(p) for p in input().split()])

food_bought = 0

while amount_of_money and food_prices:
    current_money = amount_of_money[-1]
    current_price = food_prices[0]

    if current_money == current_price:
        food_bought += 1
        amount_of_money.pop()
        food_prices.popleft()

    elif current_money > current_price:
        food_bought += 1
        diff = current_money - current_price
        food_prices.popleft()
        amount_of_money.pop()
        if amount_of_money:
            amount_of_money[-1] += diff

    elif current_money < current_price:
        amount_of_money.pop()
        food_prices.popleft()

if food_bought >= 4:
    print(f"Gluttony of the day! Henry ate {food_bought} foods.")
elif food_bought == 1:
    print(f"Henry ate: 1 food.")
elif food_bought > 1:
    print(f"Henry ate: {food_bought} foods.")
else:
    print(f"Henry remained hungry. He will try next weekend again.")