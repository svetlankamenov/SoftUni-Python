import re

text = input().lower()
keyword = input().lower()

pattern = fr"\b{keyword}\b"

matches = re.findall(pattern, text)

print(len(matches))