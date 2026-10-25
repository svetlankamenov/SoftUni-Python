new_string = ""
words = input().split(" ")

for word in words:
    new_string += word * len(word)

print(new_string)