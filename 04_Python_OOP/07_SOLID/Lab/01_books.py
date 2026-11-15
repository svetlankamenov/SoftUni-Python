class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book:Book):
        if book not in self.books:
            self.books.append(book)
            return "Book added successfully"

        return "Book is already added"

    def find_book(self, title):
        try:
            book = [b for b in self.books if b.title == title][0]
        except IndexError:
            return "Book not found"

        return f"{book.title} by {book.author}"