from modules.modules_lab.mathematical_operations.core import math_operations

expression = input().split()

first_num = float(expression[0])
second_num = float(expression[2])
sign = expression[1]
result = math_operations(first_num, second_num, sign)
print(f"{result:.2f}")