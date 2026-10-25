def calculator(a: int, b: int, operator: str):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return int(a / b)

operation = input()
first_number = int(input())
second_number = int(input())

print(calculator(first_number, second_number, operation))