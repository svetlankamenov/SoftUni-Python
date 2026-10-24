max_number = 0
flag = 1
number = ""

while True:
    number = input()

    if number == "Stop":
        break

    number = int(number)

    if flag == 1:
        max_number = number
        flag = 0
    elif number > max_number:
        max_number = number

print(max_number)