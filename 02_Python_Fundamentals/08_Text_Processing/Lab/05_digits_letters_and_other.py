characters = {"digits": "", "letters": "", "other" : ""}

string = input()
for ch in string:
    if "a" <= ch.lower() <= "z":
        characters["letters"] += ch
    elif "0" <= ch <= "9":
        characters["digits"] += ch
    else:
        characters["other"] += ch

print(characters["digits"])
print(characters["letters"])
print(characters["other"])