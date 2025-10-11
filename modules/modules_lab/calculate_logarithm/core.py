from math import log

def log_num(num, base=None):
    if base is not None:
        return f"{log(num, base):.2f}"
    return f"{log(num):.2f}"