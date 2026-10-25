def is_long_enough(password):
    if 6 <= len(password) <= 10:
        return True
    else:
        return False

def characters_check(password):
    flag = False
    for char in password:
        if not ("a" <= char <= "z" or "A" <= char <= "Z" or "0" <= char <= "9"):
            flag = False
            break
        else:
            flag = True

    return flag

def digits_check(password):
    flag = False
    digits_count = 0
    for char in password:
        if char.isdigit():
            digits_count += 1
        if digits_count == 2:
            flag = True
            break
        else:
            flag = False

    return flag

def password_validator(password):
    if is_long_enough(password) and characters_check(password) and digits_check(password):
        print("Password is valid")
    else:
        if not is_long_enough(password):
            print("Password must be between 6 and 10 characters")
        if not characters_check(password):
            print("Password must consist only of letters and digits")
        if not digits_check(password):
            print("Password must have at least 2 digits")

user_input = input()
password_validator(user_input)