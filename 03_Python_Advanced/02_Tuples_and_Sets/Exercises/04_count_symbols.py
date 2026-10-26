characters = {}

text = tuple(input())

for char in text:
    if char not in characters:
        characters[char] = text.count(char)

sorted_characters = {k: v for k, v in sorted(characters.items(), key=lambda item: item[0])}

for char, count in sorted_characters.items():
    print(f"{char}: {count} time/s")