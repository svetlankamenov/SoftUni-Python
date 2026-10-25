def smallest_of_three_numbers(a: int, b: int, c: int):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < a and c < b:
        return c

first_number = int(input())
second_number = int(input())
third_number = int(input())
print(smallest_of_three_numbers(first_number, second_number, third_number))