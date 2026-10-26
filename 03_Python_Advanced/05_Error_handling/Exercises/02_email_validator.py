class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

while True:
    email = input()
    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")
    else:
        name, domain = email.split("@")
        if len(name) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")
        else:
            if (domain.endswith(".com") or domain.endswith(".bg")
                or domain.endswith(".net") or domain.endswith(".org")):
                print("Email is valid")
            else:
                raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")