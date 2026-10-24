min_number = 0
flag = 1
number = ""

while True:
    number = input()

    if number == "Stop":
        break

    number = int(number)

    if flag == 1:
        min_number = number
        flag = 0
    elif number < min_number:
        min_number = number

print(min_number)