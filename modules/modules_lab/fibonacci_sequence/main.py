from modules.modules_lab.fibonacci_sequence.core import create_sequence, locate

commands = input()
sequence = None

while commands != "Stop":
    num = int(commands.split()[-1])

    if commands.startswith("Create"):
        sequence = create_sequence(num)
        print(*sequence)
    else:
        if sequence:
            print(locate(num, sequence))
        else:
            print(f"Please initialize a sequence")

    commands = input()