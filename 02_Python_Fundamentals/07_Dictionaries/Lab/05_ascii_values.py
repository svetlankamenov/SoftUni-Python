list_of_characters = input().split(", ")
ASCII_values = {ch:ord(ch) for ch in list_of_characters}

print(ASCII_values)