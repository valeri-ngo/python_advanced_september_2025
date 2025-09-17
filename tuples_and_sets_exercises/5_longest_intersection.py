num = int(input())

longest_intersection = set()

for _ in range(num):

    intersection_input = input().split('-')
    first_split = intersection_input[0]
    second_split = intersection_input[1]

    first_start, first_end = map(int, first_split.split(','))
    second_start, second_end = map(int, second_split.split(','))

    first_set = set(range(first_start, first_end + 1))
    second_set = set(range(second_start, second_end + 1))

    intersection = first_set & second_set

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is {list(sorted(longest_intersection))} with length {len(longest_intersection)}")
