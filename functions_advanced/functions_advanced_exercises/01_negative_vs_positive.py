def stats(*args):
    positives = sum([x for x in args if x > 0])
    negatives = sum([x for x in args if x < 0])
    result = f"{negatives}\n{positives}\n"

    if abs(negatives) > positives:
        result += "The negatives are stronger than the positives"
    else:
        result += "The positives are stronger than the negatives"
    return result

nums = [int(x) for x in input().split()]
print(stats(*nums))
