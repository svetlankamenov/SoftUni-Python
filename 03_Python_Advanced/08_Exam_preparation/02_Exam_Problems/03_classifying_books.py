def classify_books(*args, **kwargs):
    fiction_books = {}
    non_fiction_books = {}
    output = ""

    for book_type, book_name in args:
        for code, name in kwargs.items():
            if book_name == name:
                if book_type == "fiction":
                    fiction_books[code] = name
                elif book_type == "non_fiction":
                    non_fiction_books[code] = name

    fiction_books = dict(sorted(fiction_books.items(), key=lambda x: x[0]))
    non_fiction_books = dict(sorted(non_fiction_books.items(), key=lambda x: x[0], reverse=True))

    if fiction_books:
        output += "Fiction Books:\n"
        for code, name in fiction_books.items():
            output += f"~~~{code}#{name}\n"

    if non_fiction_books:
        output += "Non-Fiction Books:\n"
        for code, name in non_fiction_books.items():
            output += f"***{code}#{name}\n"

    output = output.rstrip()

    return output