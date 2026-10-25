def sum_numbers(a: int, b: int):
    return a + b

def substract(result: int, c: int):
    return result - c

def add_and_substract(a, b, c):
    return substract(sum_numbers(a, b), c)

first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_substract(first_number, second_number, third_number))