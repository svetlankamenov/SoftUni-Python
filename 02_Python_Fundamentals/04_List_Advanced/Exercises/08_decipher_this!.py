def deciphering(words:list):
    deciphered_words = []
    number = ""
    for word in words:
        for i in word:
            if i in "0123456789":
                number += i
        new_word = chr(int(number))

        word = word[len(number):]
        word = list(word)
        word[0], word[-1] = word[-1], word[0]
        word = "".join(word)
        new_word += word

        deciphered_words.append(new_word)

        number = ""

    return deciphered_words

secret_message = input().split(" ")
print(*deciphering(secret_message))