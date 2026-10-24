max_first_digit = int(input())
max_second_digit = int(input())
max_third_digit = int(input())

for first_digit in range(1, max_first_digit + 1):
    for second_digit in range(1, max_second_digit + 1):
        for third_digit in range(1, max_third_digit + 1):

            if first_digit % 2 == 0 and third_digit % 2 == 0 and second_digit in (2, 3, 5, 7):
                print(f"{first_digit} {second_digit} {third_digit}")