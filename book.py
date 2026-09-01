import re
from datetime import date

class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = None # placeholder, actual value set via set_isbn()
        self.set_isbn(isbn)
        self.date_added = date.today()
        self.is_borrowed = False

    def display_info(self):
        return f"{self.title} by {self.author} {self.year} - ISBN: {self.isbn}"

    def set_isbn(self, isbn):
        if not re.match(r'^\d{13}$', isbn):
            raise ValueError("ISBN must be 13 digits")

        self.isbn = isbn

class EBook(Book):
    def __init__(self, title, author, year, isbn, file_size_mb):
        super().__init__(title, author, year, isbn)
        self.file_size_mb = file_size_mb

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info} | File size: {self.file_size_mb}MB"

if __name__ == "__main__":
    try:
        book1 = Book("The Hobbit", "J.R.R. Tolkien", 1937, "9780345339688")
        print(book1.display_info())

        ebook1 = EBook("Atomic Habits", "James Clear", 2018, "9780735211292", 4.5)
        print(ebook1.display_info())

    except ValueError as e:
        print(e)