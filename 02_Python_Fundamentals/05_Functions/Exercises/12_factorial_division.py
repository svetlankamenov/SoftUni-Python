def factorial_division(a: int, b: int):
    first_num_factorial = 1
    second_num_factorial = 1

    for i in range(1, a+1):
        first_num_factorial *= i
    for i in range(1, b+1):
        second_num_factorial *= i

    return first_num_factorial / second_num_factorial

first_number = int(input())
second_number = int(input())
print(f"{factorial_division(first_number, second_number):.2f}")