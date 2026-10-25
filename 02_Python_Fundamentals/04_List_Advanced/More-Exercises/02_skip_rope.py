user_input = input()
numbers_lst = [num for num in user_input if "0" <= num <= "9"]
numbers_lst = list(map(int, numbers_lst))
non_numbers = [chr for chr in user_input if not "0" <= chr <= "9"]

take_lst = [num for i, num in enumerate(numbers_lst) if i % 2 == 0]
skip_lst = [num for i, num in enumerate(numbers_lst) if i % 2 != 0]

new_string = ""
index = 0

for i in range(len(take_lst)):
    for j in range(take_lst[i]):
        new_string += non_numbers[index]
        index += 1

    index += skip_lst[i]

print(new_string)