def translate(char: str, replacement: str, string: str):
    new_string = string.replace(char, replacement)
    print(new_string)

    return new_string

def find_last_index(char: str, string: str):
    index = 0
    for i, ch in enumerate(string):
        if ch == char:
            index = i

    print(index)

def remove_elements(start: int, count: int, string: str):
    new_string = string[:start] + string[start + count:]
    print(new_string)

text = input()

while True:
    command = input()
    if command == "End":
        break

    command = command.split(" ")

    if command[0] == "Translate":
        text = translate(command[1], command[2], text)

    elif command[0] == "Includes":
        if command[1] in text:
            print(True)
        else:
            print(False)

    elif command[0] == "Start":
        print(text.startswith(command[1]))

    elif command[0] == "Lowercase":
        text = text.lower()
        print(text)

    elif command[0] == "FindIndex":
        find_last_index(command[1], text)

    elif command[0] == "Remove":
        remove_elements(int(command[1]), int(command[2]), text)