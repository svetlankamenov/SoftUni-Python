emoticons = []

text = input()

for i in range(len(text)):
    if text[i] == ":":
        emoticons.append(text[i] + text[i+1])

for emoji in emoticons:
    print(emoji)