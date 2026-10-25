import re

pattern = r"\b_[A-Za-z0-9]+\b"
text = input()

matches = re.findall(pattern, text)
matches = [re.sub(r"_", "", match) for match in matches]

print(",".join(matches))