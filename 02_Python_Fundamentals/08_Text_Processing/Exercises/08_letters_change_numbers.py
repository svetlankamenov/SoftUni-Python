def calculate_expression(expression: str):
    sum = 0
    first_symbol = expression[0]
    last_symbol = expression[-1]
    number = expression[1:-1]
    number = int(number)

    index_of_first_letter = (ord(first_symbol.upper()) - ord('A')) + 1
    index_of_last_letter = (ord(last_symbol.upper()) - ord('A')) + 1

    if first_symbol.isupper():
        sum += number / index_of_first_letter
    else:
        sum += number * index_of_first_letter

    if last_symbol.isupper():
        sum = sum - index_of_last_letter
    else:
        sum = sum + index_of_last_letter

    return sum

total_sum = 0

strings = input().split()
for string in strings:
    total_sum += calculate_expression(string)

print(f"{total_sum:.2f}")