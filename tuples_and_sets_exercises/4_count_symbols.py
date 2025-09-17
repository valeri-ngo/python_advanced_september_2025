from collections import Counter

text = list(input())

counter = Counter(text)

for char in sorted(counter):
    print(f"{char}: {counter[char]} time/s")
