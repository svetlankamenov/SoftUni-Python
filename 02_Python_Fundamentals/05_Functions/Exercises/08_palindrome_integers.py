def is_palindrome(num: int):
    num = str(num)

    if len(num) == 1:
        return True

    for i in range(len(num)//2):
        if num[i] != num[len(num)-i-1]:
            return False
        else:
            return True

user_input = input().split(", ")
numbers = []
for number in user_input:
    numbers.append(int(number))

for number in numbers:
    print(is_palindrome(number))