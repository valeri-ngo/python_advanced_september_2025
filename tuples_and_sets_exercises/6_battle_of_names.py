number = int(input())

odd_set = set()
even_set = set()

for row_idx in range(1, number + 1):
    names = input()
    count = 0

    for char in names:
        count += ord(char)

    result = count // row_idx

    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

sum_odd = sum(odd_set)
sum_even = sum(even_set)

if sum_odd == sum_even:
    result = odd_set | even_set
elif sum_odd > sum_even:
    result = odd_set - even_set
else:
    result = odd_set ^ even_set

print(', '.join(map(str, result)))