reversed_word = ""

while True:
    word = input()
    if word == "end":
        break

    for i in range(len(word)-1, -1, -1):
        reversed_word += word[i]

    print(f"{word} = {reversed_word}")
    reversed_word = ""