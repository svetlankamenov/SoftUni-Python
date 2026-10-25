import re

pattern = r"!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]"

n = int(input())

for _ in range(n):
    line = input()
    matches = re.findall(pattern, line)

    if matches:
        command, text = matches[0]
        translated_symbols = []
        for ch in text:
            translated_symbols.append(str(ord(ch)))
        print(f"{command}: ", end="")
        print(" ".join(translated_symbols))
    else:
        print("The message is invalid")