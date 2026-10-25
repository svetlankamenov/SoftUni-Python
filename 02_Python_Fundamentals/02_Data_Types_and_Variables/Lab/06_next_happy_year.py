digits = []

year = int(input())

while True:
    year += 1
    new_year = year

    while new_year > 0:
        digits.append(new_year % 10)
        new_year //= 10

    digits.reverse()

    if len(digits) == len(set(digits)):
        for digit in digits:
            print(digit, end="")
        break

    digits.clear()