mapper = {
    "/": lambda num1, num2: num1 / num2,
    "*": lambda num1, num2: num1 * num2,
    "-": lambda num1, num2: num1 - num2,
    "+": lambda num1, num2: num1 + num2,
    "^": lambda num1, num2: num1 ** num2
}

def math_operations(num1, num2, sign):
    function = mapper[sign]
    return function(num1, num2)