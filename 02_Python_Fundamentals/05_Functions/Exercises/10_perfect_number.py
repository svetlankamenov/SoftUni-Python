import math

def is_perfect_number(num: int):
    proper_divisors_sum = 0

    for i in range(1, num):
        if num % i == 0:
            proper_divisors_sum += i

    if proper_divisors_sum == num:
        return True
    else:
        return False

number = int(input())
if is_perfect_number(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")