import re

words = {}

file_with_words = open("words.txt", "r")
for line in file_with_words:
    for word in line.split():
        words[word] = 0

file_with_words.close()

file_with_text = open("input.txt", "r")
for word in words:
    for line in file_with_text:
        words[word] += len(re.findall(rf"\b{re.escape(word.lower())}\b", line.lower()))
    file_with_text.seek(0)

file_with_text.close()

words = dict(sorted(words.items(), key=lambda x: x[1], reverse=True))

new_file = open("output.txt", "w")
for word, count in words.items():
    new_file.write(f"{word} - {count}\n")

new_file.close()