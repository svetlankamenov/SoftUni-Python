def characters_in_range(first_char: str, second_char: str):
    characters = []
    for symbol in range(ord(first_char)+1, ord(second_char)):
        characters.append(chr(symbol))
    return characters

first_character = input()
second_character = input()

print(*characters_in_range(first_character, second_character), " ")