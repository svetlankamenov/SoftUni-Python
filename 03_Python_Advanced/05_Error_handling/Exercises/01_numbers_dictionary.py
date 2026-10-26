numbers_dictionary = {}

while True:
    line = input()
    if line == "Search":
        break

    number_as_string = line

    try:
        number = int(input())
    except ValueError:
        print("The variable number must be an integer")
        continue

    numbers_dictionary[number_as_string] = number

while True:
    line = input()
    if line == "Remove":
        break

    try:
        print(numbers_dictionary[line])
    except KeyError:
        print("Number does not exist in dictionary")
        continue

while True:
    line = input()
    if line == "End":
        break

    try:
        del numbers_dictionary[line]
    except KeyError:
        print("Number does not exist in dictionary")
        continue

print(numbers_dictionary)