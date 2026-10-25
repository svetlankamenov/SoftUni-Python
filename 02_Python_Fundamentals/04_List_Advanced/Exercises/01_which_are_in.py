keywords = input().split(", ")
random_words = input().split(", ")
filtered_words = []

for word in keywords:
    for i in random_words:
        if word in i:
            if word not in filtered_words:
                filtered_words.append(word)

print(filtered_words)