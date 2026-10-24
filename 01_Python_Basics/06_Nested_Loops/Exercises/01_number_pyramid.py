n = int(input())
numbers_on_row = 1
current_number = 1

while numbers_on_row <= n:

    for i in range(numbers_on_row):
        print(current_number, end=" ")
        current_number += 1
        if current_number > n:
            break

    print()
    if current_number > n:
        break
    numbers_on_row += 1