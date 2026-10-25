def move_letters(string: str, count: int):
    new_string = string[count:] + string[:count]
    return new_string

def insert_letter(string: str, i: int, letter: str):
    new_string = string[:i] + letter + string[i:]
    return new_string

def change_letters(string: str, substr: str, new_letter: str):
    new_string = ""

    for letter in string:
        if letter == substr:
            new_string += new_letter
        else:
            new_string += letter

    return new_string

encrypted_message = input()

while True:
    instruction = input()
    if instruction == "Decode":
        print(f"The decrypted message is: {encrypted_message}")
        break

    instruction = instruction.split("|")

    if instruction[0] == "Move":
        letters_num = int(instruction[1])
        encrypted_message = move_letters(encrypted_message, letters_num)

    elif instruction[0] == "Insert":
        index = int(instruction[1])
        value = instruction[2]
        encrypted_message = insert_letter(encrypted_message, index, value)

    elif instruction[0] == "ChangeAll":
        substring = instruction[1]
        replacement = instruction[2]
        encrypted_message = change_letters(encrypted_message, substring, replacement)