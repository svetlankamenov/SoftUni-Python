doubled_char = ""

while True:
    string = input()
    if string == "End":
        break
    elif string == "SoftUni":
        continue

    for i in string:
        doubled_char += i * 2

    print(doubled_char)
    doubled_char = ""