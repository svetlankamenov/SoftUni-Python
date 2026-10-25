max_number = 0

for i in range(3):
    number = int(input())

    if i == 0:
        max_number = number
    elif number > max_number:
        max_number = number

print(max_number)