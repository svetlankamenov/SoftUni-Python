import re

pattern = r"(?<!\S)-?(?:0|[1-9]\d*)(?:\.\d+)?(?!\S)"
text = input()

numbers = re.findall(pattern, text)
for number in numbers:
    print(number, end=" ")