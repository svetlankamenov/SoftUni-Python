vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

user_input = input()
no_vowel_string = [x for x in user_input if x not in vowels]

for x in no_vowel_string:
    print(x, end="")