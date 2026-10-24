secret_command = ""
found_c = False
found_o = False
found_n = False

while True:
    word = input()
    #Игнориране на всичко различно от латински букви
    if not ("A" <= word <= "Z" or "a" <= word <= "z"):
        continue

    if found_c and found_o and found_n:
        print(secret_command, end=" ")
        found_c = False
        found_o = False
        found_n = False
        secret_command = ""

    # Край на въвеждането
    if word == "End":
        break

    if word == "c" and found_c == False:
        found_c = True
        continue
    elif word == "o" and found_o == False:
        found_o = True
        continue
    elif word == "n" and found_n == False:
        found_n = True
        continue
    elif word != "End":
        secret_command += word