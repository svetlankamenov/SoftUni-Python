searched_book = input()
book_count = 0

while True:
    book = input()
    book_count += 1

    if book == searched_book:
        book_count -= 1
        print(f"You checked {book_count} books and found it.")
        break
    if book == "No More Books":
        book_count -= 1
        print("The book you search is not here!")
        print(f"You checked {book_count} books.")
        break