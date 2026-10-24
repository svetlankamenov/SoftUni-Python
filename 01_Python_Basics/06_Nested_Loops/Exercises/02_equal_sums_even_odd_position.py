first_number = int(input())
last_number = int(input())
sum_of_even_positions = 0
sum_of_odd_positions = 0

for current_number in range(first_number, last_number + 1):
    current_number = str(current_number)
    sum_of_odd_positions = int(current_number[0]) + int(current_number[2]) + int(current_number[4])
    sum_of_even_positions = int(current_number[1]) + int(current_number[3]) + int(current_number[5])

    if sum_of_odd_positions == sum_of_even_positions:
        print(current_number, end=" ")