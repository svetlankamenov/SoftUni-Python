import re

string_pattern = r"[A-Z-a-z]+"
number_pattern = r"\b[0-9]+\b"

first_sequence = set(map(int, input().split(" ")))
second_sequence = set(map(int, input().split(" ")))

n = int(input())

for _ in range(n):
    line = input()
    command = re.findall(string_pattern, line)
    command = command[0] + " " + command[1]
    numbers = re.findall(number_pattern, line)

    if command == "Add First":
        for num in numbers:
            first_sequence.add(int(num))
    elif command == "Add Second":
        for num in numbers:
            second_sequence.add(int(num))
    elif command == "Remove First":
        for num in numbers:
            if int(num) in first_sequence:
                first_sequence.remove(int(num))
    elif command == "Remove Second":
        for num in numbers:
            if int(num) in second_sequence:
                second_sequence.remove(int(num))
    elif command == "Check Subset":
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print(True)
        else:
            print(False)
first_sequence = sorted(first_sequence)
second_sequence = sorted(second_sequence)
print(", ".join(map(str, first_sequence)))
print(", ".join(map(str, second_sequence)))