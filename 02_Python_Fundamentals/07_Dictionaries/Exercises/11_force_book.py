force_book = {}

def add_user(side: str, user: str, book: dict):
    is_in = False
    if side not in book:
        book[side] = []

    for names in book.values():
        if user in names:
            is_in = True

    if is_in:
        pass
    else:
        book[side].append(user)

    return book

def change_side(new_side: str, user: str, book: dict):
    is_in = False
    old_side = ""
    for sides, names in book.items():
        if user in names:
            is_in = True
            old_side = sides

    if new_side not in book and not is_in:
        book[new_side] = [user]
    elif new_side in book and not is_in:
        book[new_side].append(user)
    elif new_side in book and is_in:
        book[old_side].remove(user)
        book[new_side].append(user)
    elif new_side not in book and is_in:
        book[new_side] = [user]
        book[old_side].remove(user)

    print(f"{user} joins the {new_side} side!")

    return book

def print_book(book: dict):
    for side, users in book.items():
        if len(users) >= 1:
            print(f"Side: {side}, Members: {len(users)}")
            for user in users:
                print(f"! {user}")

while True:
    line = input()
    if line == "Lumpawaroo":
        print_book(force_book)
        break

    if " | " in line:
        force_side, user_name = line.split(" | ")
        force_book = add_user(force_side, user_name, force_book)

    elif " -> " in line:
        user_name, force_side = line.split(" -> ")
        force_book = change_side(force_side, user_name, force_book)