number_one = int(input())
number_two = int(input())
operation = input()
result = 0

if operation == "+":
    number_type = ""
    result = number_one + number_two

    if result % 2 == 0:
        number_type = "even"
    else:
        number_type = "odd"

    print(f"{number_one} {operation} {number_two} = {result} - {number_type}")

elif operation == "-":
    number_type = ""
    result = number_one - number_two

    if result % 2 == 0:
        number_type = "even"
    else:
        number_type = "odd"

    print(f"{number_one} {operation} {number_two} = {result} - {number_type}")

elif operation == "*":
    number_type = ""
    result = number_one * number_two

    if result % 2 == 0:
        number_type = "even"
    else:
        number_type = "odd"

    print(f"{number_one} {operation} {number_two} = {result} - {number_type}")

elif operation == "/":

    if not number_two == 0:
        result = number_one / number_two
        print(f"{number_one} / {number_two} = {result:.2f}")
    else:
        print(f"Cannot divide {number_one} by zero")

elif operation == "%":
    if not number_two == 0:
        result = number_one % number_two
        print(f"{number_one} % {number_two} = {result}")
    else:
        print(f"Cannot divide {number_one} by zero")