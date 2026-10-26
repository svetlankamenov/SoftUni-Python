def operate(operator: str, *args):
    if operator == "+":
        result = 0
        for number in args:
            result += number

    elif operator == "-":
        result = args[0]
        for i in range(1, len(args)):
            result -= args[i]

    elif operator == "*":
        result = 1
        for number in args:
            result *= number

    elif operator == "/":
        result = args[0]
        for i in range(1, len(args)):
            result /= args[i]

    return result