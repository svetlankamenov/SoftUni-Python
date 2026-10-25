even_numbers = []
odd_numbers = []
positive_numbers = []
negative_numbers = []

n = int(input())

for _ in range(n):
    number = int(input())

    if number >= 0:
        positive_numbers.append(number)
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    else:
        negative_numbers.append(number)
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

command = input()

if command.lower() == "even":
    print(even_numbers)
elif command.lower() == "odd":
    print(odd_numbers)
elif command.lower() == "positive":
    print(positive_numbers)
elif command.lower() == "negative":
    print(negative_numbers)