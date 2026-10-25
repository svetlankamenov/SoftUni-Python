new_string = ""
temp_char = ""
temp_number = ""
characters = []
unique_symbols = []

string = input()

for index, ch in enumerate(string):
    if not ch.isdigit():
        temp_char += ch
    else:
        temp_number += ch
        if index == len(string) - 1 or not string[index + 1].isdigit():
            characters.append((temp_char, int(temp_number)))
            temp_char = ""
            temp_number = ""

for char, count in characters:
    new_string += char.upper() * count

for ch in new_string:
    if ch not in unique_symbols:
        unique_symbols.append(ch)

print(f"Unique symbols used: {len(unique_symbols)}")
print(new_string)