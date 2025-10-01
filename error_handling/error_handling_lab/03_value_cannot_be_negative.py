class ValueCannotBeNegative(Exception):
    pass

for _ in range(5):
    integers = int(input())
    if integers < 0:
        raise ValueCannotBeNegative
