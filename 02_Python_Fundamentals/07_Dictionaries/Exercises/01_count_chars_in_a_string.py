characters = {}

user_input = input()

for char in user_input:
    if char == " ":
        pass
    elif char not in characters:
        characters[char] = 1
    else:
        characters[char] += 1

for char, count in characters.items():
    print(f"{char} -> {count}")