phonebook = {}

while True:
    contact_info = input()

    if "-" in contact_info:
        name, phone_number = contact_info.split("-")
        phonebook[name] = phone_number

    else:
        n = int(contact_info)

        for _ in range(n):
            name = input()
            if name in phonebook:
                print(f"{name} -> {phonebook[name]}")
            else:
                print(f"Contact {name} does not exist.")

        break