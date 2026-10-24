import math

sum_of_prime_numbers = 0
sum_of_nonprime_numbers = 0
is_prime = True

while True:
    number = input()
    if number == "stop":
        print(f"Sum of all prime numbers is: {sum_of_prime_numbers}")
        print(f"Sum of all non prime numbers is: {sum_of_nonprime_numbers}")
        break

    number = int(number)

    if number < 0:
        print("Number is negative.")
        continue

    for i in range(2, math.ceil(math.sqrt(number)) + 1):
        if number % i == 0:
            is_prime = False

    if number == 0:
        is_prime = False
    if number == 1 or number == 2:
        is_prime = True

    if is_prime:
        sum_of_prime_numbers += number
    else:
        sum_of_nonprime_numbers += number

    is_prime = True