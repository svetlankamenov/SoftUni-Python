import re

pattern = r"(\b\d{2}[\/][A-Z]{1}[a-z]{2}[\/]\d{4}\b|\b\d{2}[-][A-Z]{1}[a-z]{2}[-]\d{4}\b|\b\d{2}[.][A-Z]{1}[a-z]{2}[.]\d{4}\b)"
text = input()

dates = re.findall(pattern, text)

for date in dates:
    day, month, year = re.split(r"[/.-]", date)
    print(f"Day: {day}, Month: {month}, Year: {year}")