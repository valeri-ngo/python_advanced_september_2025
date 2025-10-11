def create_sequence(num):
    seq = [0, 1]

    for _ in range(num -2):
        seq.append(seq[-1] + seq[-2])
    return seq

def locate(num, seq):
    try:
        index = seq.index(num)
        return f"The number - {num} is at index {index}"
    except ValueError:
        return f"The number {num} is not in the sequence"