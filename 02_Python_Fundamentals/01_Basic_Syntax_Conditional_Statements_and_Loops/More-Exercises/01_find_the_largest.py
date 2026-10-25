largest_number = ""
number = input()
max_digit = 0
seen_indexes = ""
last_index = 0

while True:
    if len(seen_indexes) == len(number):
        break

    for i in range(len(number)):
        if int(number[i]) > max_digit and str(i) not in seen_indexes:
            max_digit = int(number[i])
            last_index = i

    largest_number += str(max_digit)
    seen_indexes += str(last_index)
    max_digit = 0
    last_index = 0

print(largest_number)