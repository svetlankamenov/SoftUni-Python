number = int(input())
is_special = True

for num_to_str in range(1111, 10000):

    for digit in str(num_to_str):
        if int(digit) == 0:
            is_special = False
            break
        elif number % int(digit) != 0:
            is_special = False

    if is_special:
        print(num_to_str, end=" ")
    is_special = True