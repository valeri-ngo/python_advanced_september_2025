expression = input()

parenthesis = {
    "(": ")",
    "[": "]",
    "{": "}"
    }

stack = []

for char in expression:
    if char in parenthesis:
        stack.append(char)
    elif char in parenthesis.values():
        if not stack:
            print("NO")
            break
        last_opening_parenthesis = stack.pop()
        if parenthesis[last_opening_parenthesis] != char:
            print("NO")
            break
else:
    if stack:
        print("NO")
    else:
        print("YES")