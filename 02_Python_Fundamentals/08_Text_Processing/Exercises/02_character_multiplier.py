sum = 0

strings = input().split(" ")
if len(strings[0]) >= len(strings[1]):
    bigger = strings[0]
    smaller = strings[1]
else:
    bigger = strings[1]
    smaller = strings[0]

for i in range(len(smaller)):
    sum += ord(bigger[i]) * ord(smaller[i])

bigger = bigger[len(smaller):]

for i in range(len(bigger)):
    sum += ord(bigger[i])

print(sum)