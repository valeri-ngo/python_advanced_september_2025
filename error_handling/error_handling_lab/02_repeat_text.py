first_input = input()

try:
    second_text = int(input())

except ValueError:
    print("Variable times must be an integer")
else:
    print(first_input * second_text)