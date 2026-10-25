def sum_of_odd_and_even_digits(number: str):
    even_digits = []
    odd_digits = []

    for digit in number:
        if int(digit) % 2 == 0:
            even_digits.append(int(digit))
        else:
            odd_digits.append(int(digit))

    return  sum(odd_digits), sum(even_digits)

user_input = input()

print(f"Odd sum = {sum_of_odd_and_even_digits(user_input)[0]}, Even sum = {sum_of_odd_and_even_digits(user_input)[1]}")