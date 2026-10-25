encrypted_string = ""

string = input()

for ch in string:
    encrypted_string += chr(ord(ch) + 3)

print(encrypted_string)