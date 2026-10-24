import math

best_word = ""
best_score = 0
current_score = 0

while True:
    word = input()
    if word == "End of words":
        break

    for i in word:
        current_score += ord(i)

    if word[0] in ("a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"):
        current_score *= len(word)
    else:
        current_score = math.floor(current_score / len(word))

    if current_score > best_score:
        best_score = current_score
        best_word = word

    current_score = 0

print(f"The most powerful word is {best_word} - {best_score}")