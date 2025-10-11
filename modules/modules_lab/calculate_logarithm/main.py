from modules.modules_lab.calculate_logarithm.core import log_num

number = int(input())
try:
    base = int(input())
    print(log_num(number, base))
except ValueError:
    print(log_num(number))
