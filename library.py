import json
from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Book objects can be added to the library")

        self.books.append(book)

    def remove_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                self.books.remove(b)
                return

        raise ValueError(f"No book found with ISBN {isbn}")

    def search_book(self, keyword):
        results = []
        for b in self.books:
            keyword_lower = keyword.lower()
            if (keyword_lower in b.title.lower()
                    or keyword_lower in b.author.lower()
                    or keyword_lower in b.isbn):
                results.append(b)
        return results

    def save_books(self, filename):
        data = []

        for b in self.books:
            data.append({"title": b.title, "author": b.author, "year": b.year, "isbn": b.isbn})

        with open(filename, "w") as f:
            json.dump(data, f)

    def load_books(self, filename):
        with open(filename) as f:
            data = json.load(f)

        self.books = []

        for item in data:
            book = Book(item["title"], item["author"], item["year"], item["isbn"])
            self.books.append(book)

    def borrow_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
              if b.is_borrowed:
                  raise ValueError(f"Book with ISBN {isbn} is already borrowed.")
              b.is_borrowed = True
              return

        raise ValueError(f"No book found with ISBN {isbn}.")