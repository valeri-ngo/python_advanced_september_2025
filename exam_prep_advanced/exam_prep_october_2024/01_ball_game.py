from collections import deque

strength = [int(x) for x in input().split()]
accuracy = deque([int(x) for x in input().split()])
sum_goals = 0


while strength and accuracy:

    current_strength = strength[-1]
    current_accuracy = accuracy[0]

    result = current_accuracy + current_strength

    if result == 100:
        strength.pop()
        accuracy.popleft()
        sum_goals += 1

    elif result < 100:
        if current_strength < current_accuracy:
            strength.pop()
        elif current_strength > current_accuracy:
            accuracy.popleft()
        else:
            strength[-1] += current_accuracy
            accuracy.popleft()
    else:
        strength[-1] -= 10
        temp = accuracy.popleft()
        accuracy.append(temp)

if sum_goals == 3:
    print(f"Paul scored a hat-trick!")
elif sum_goals == 0:
    print(f"Paul failed to score a single goal.")
elif sum_goals > 3:
    print(f"Paul performed remarkably well!")
elif 0 < sum_goals < 3:
    print(f"Paul failed to make a hat-trick.")

if sum_goals:
    print(f"Goals scored: {sum_goals}")

if strength or accuracy:
    if strength:
        print(f"Strength values left: {', '.join([str(x) for x in strength])}")
    elif accuracy:
        print(f"Accuracy values left: {', '.join(str(x) for x in accuracy)}")