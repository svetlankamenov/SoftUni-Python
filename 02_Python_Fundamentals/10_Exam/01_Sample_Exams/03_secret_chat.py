def insert_space(i: int, string: str):
    new_string = string[:i] + " " + string[i:]
    print(new_string)
    return new_string

def reverse_string(substring: str, string: str):
    if substring in string:
        new_string = string.replace(substring, "", 1)
        new_string += substring[::-1]
        print(new_string)
        return new_string
    else:
        print("error")
        return string

def change_all(substring: str, new_letter, string: str):
    new_string = string.replace(substring, new_letter)

    print(new_string)
    return new_string

message = input()

while True:
    command = input()
    if command == "Reveal":
        print(f"You have a new text message: {message}")
        break

    command = command.split(":|:")
    if command[0] == "InsertSpace":
        message = insert_space(int(command[1]), message)

    elif command[0] == "Reverse":
        message = reverse_string(command[1], message)

    elif command[0] == "ChangeAll":
        message = change_all(command[1], command[2], message)