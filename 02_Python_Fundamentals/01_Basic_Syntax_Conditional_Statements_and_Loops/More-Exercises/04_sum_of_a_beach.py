words = ["sand", "water", "fish", "sun"]
appearing_times = 0

string = input().lower()

for word in words:
    appearing_times += string.count(word)

print(appearing_times)