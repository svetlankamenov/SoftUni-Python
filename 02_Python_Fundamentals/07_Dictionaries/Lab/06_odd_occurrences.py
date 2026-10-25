dictionary = {}
result = ""

user_input = input().split(" ")

for word in user_input:
    if word.lower() not in dictionary:
        dictionary[word.lower()] = 1
    else:
        dictionary[word.lower()] += 1

for word, count in dictionary.items():
    if count % 2 != 0:
        print(word, end=" ")