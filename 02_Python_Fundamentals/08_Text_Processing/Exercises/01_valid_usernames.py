def is_valid_username(name: str):
    flag = True

    if not 3 <= len(name) <= 16:
        flag = False
    else:
        for ch in name:
            if not ch.isdigit() and not ch.isalpha() and not ch == "-" and not ch == "_":
                flag = False

    if flag:
        return True

valid_usernames = []

usernames = input().split(", ")

for username in usernames:
    if is_valid_username(username):
        valid_usernames.append(username)

for username in valid_usernames:
    print(username)