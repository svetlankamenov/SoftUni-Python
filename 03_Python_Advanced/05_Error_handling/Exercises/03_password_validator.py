class PasswordTooShortError(Exception):
    pass

class PasswordTooCommonError(Exception):
    pass

class PasswordNoSpecialCharactersError(Exception):
    pass

class PasswordContainsSpacesError(Exception):
    pass

def password_validator(password:str):
    special_symbols = "@*&%"
    if len(password) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters")
    elif password.isdigit() or password.isalpha() or all(ch in special_symbols for ch in password):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")
    elif not any(ch in special_symbols for ch in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")
    elif " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")
    else:
        return "Password is valid"

while True:
    password = input()
    if password == "Done":
        break

    print(password_validator(password))