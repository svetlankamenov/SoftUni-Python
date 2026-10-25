import re

pattern = r"\d+"

text = ""

while True:
    line = input()
    if line == "":
        break
    text += line + "\n"

numbers = re.findall(pattern, text)

for number in numbers:
    print(number, end=" ")