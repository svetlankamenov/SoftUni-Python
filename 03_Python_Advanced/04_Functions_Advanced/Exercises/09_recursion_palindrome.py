def palindrome(word:str, i: int):
    if i == (len(word) // 2):
        return f"{word} is a palindrome"
    else:
        if word[i] != word[len(word) - i - 1]:
            return f"{word} is not a palindrome"
        return palindrome(word, i + 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))