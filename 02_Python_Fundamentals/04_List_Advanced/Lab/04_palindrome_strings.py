palindromes = []

strings = input().split(" ")
palindrome_input = input()

for word in strings:
    if word == word[::-1]:
        palindromes.append(word)

print(palindromes)
print(f"Found palindrome {strings.count(palindrome_input)} times")