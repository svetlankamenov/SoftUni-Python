import re

pattern = r"\b[A-Za-z0-9]+(?:[._-][A-Za-z0-9]+)*@(?:[A-Za-z]+(?:-[A-Za-z]+)*\.)+[A-Za-z]+\b"

text = input()

emails = re.findall(pattern, text)
for email in emails:
    print(email)