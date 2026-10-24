count = int(input())
max_number = 0
sum_numbers = 0

for i in range(count):
    num = int(input())
    sum_numbers += num

    #Винаги първото число ще е най-голямото
    if i == 0:
        max_number = num
        continue
    #Проверка дали въведеното число е по-голямо от вече най-голямото
    if num > max_number:
        max_number = num

if max_number == sum_numbers - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    sum_numbers = sum_numbers - max_number
    print("No")
    print(f"Diff = {abs(max_number-sum_numbers)}")