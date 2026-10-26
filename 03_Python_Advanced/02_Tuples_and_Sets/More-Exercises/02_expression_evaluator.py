from collections import deque

saved_numbers = deque(list())
expression = deque(input().split(" "))


while expression:
    position = expression.popleft()
    if position.lstrip("-").isdigit():
        saved_numbers.append(int(position))
    elif position == "+":
        while len(saved_numbers) != 1:
            temp_result = saved_numbers.popleft()
            temp_result += saved_numbers.popleft()
            saved_numbers.appendleft(temp_result)
    elif position == "-":
        while len(saved_numbers) != 1:
            temp_result = saved_numbers.popleft()
            temp_result -= saved_numbers.popleft()
            saved_numbers.appendleft(temp_result)
    elif position == "*":
        while len(saved_numbers) != 1:
            temp_result = saved_numbers.popleft()
            temp_result *= saved_numbers.popleft()
            saved_numbers.appendleft(temp_result)
    elif position == "/":
        while len(saved_numbers) != 1:
            temp_result = saved_numbers.popleft()
            temp_result //= saved_numbers.popleft()
            saved_numbers.appendleft(temp_result)

print(saved_numbers[0])