import re

names = input()
pattern = r"\b[A-Z][a-z]{1,}\s\b[A-Z][a-z]{1,}\b"

valid_names = re.findall(pattern, names)
print(" ".join(valid_names))