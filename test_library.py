import pytest
import os
import json
from library import Library
from book import Book

def test_add_book_with_valid_book():
    library = Library()
    book = Book("The Hobbit", "J.R.R. Tolkien", 1937, "9780345339688")

    library.add_book(book)
    assert book in library.books

def test_add_book_with_invalid_type_raises_error():
    library = Library()
    with pytest.raises(TypeError):
        library.add_book("Not a book")

def test_remove_book_removes_existing_book():
    library = Library()
    book = Book("The Hobbit", "J.R.R. Tolkien", 1937, "9780345339688")
    library.add_book(book)

    library.remove_book("9780345339688")

    assert book not in library.books

def test_remove_book_with_missing_isbn_raises_error():
    library = Library()
    with pytest.raises(ValueError):
        library.remove_book("0000000000000")

def test_search_book_finds_match_by_title():
    library = Library()
    book = Book("The Hobbit", "J.R.R. Tolkien", 1937, "9780345339688")
    library.add_book(book)

    results = library.search_book("hobbit")

    assert book in results

def test_search_book_with_no_match_returns_empty_list():
    library = Library()
    results = library.search_book("nonexistent")
    assert results == []

def test_save_books_writes_json_file():
    library = Library()

    book = Book("The Hobbit", "J.R.R. Tolkien", 1937, "9780345339688")
    book2 = Book("1984", "George Orwell", 1949, "9780451524935")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "9780743273565")
    book4 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "9780061120084")
    book5 = Book("Brave New World", "Aldous Huxley", 1932, "9780060850524")

    library.add_book(book)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)

    library.save_books("test_books.json")

    with open("test_books.json") as f:
        saved_data = json.load(f)

    assert len(saved_data) == 5

    os.remove("test_books.json")

def test_load_books_restores_books_from_file():
    library = Library()

    book = Book("The Hobbit", "J.R.R. Tolkien", 1937, "9780345339688")
    book2 = Book("1984", "George Orwell", 1949, "9780451524935")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "9780743273565")
    book4 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "9780061120084")
    book5 = Book("Brave New World", "Aldous Huxley", 1932, "9780060850524")

    library.add_book(book)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)

    library.save_books("test_load.json")

    new_library = Library()
    new_library.load_books("test_load.json")

    assert len(new_library.books) == 5
    assert new_library.books[0].title == "The Hobbit"

    os.remove("test_load.json")

def test_borrow_book_marks_book_as_borrowed():
    # Arrange: set up a new library, add one book that is not yet borrowed
    library = Library()
    book = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997, "9780439708180")
    library.add_book(book)

    # Act: borrow that book via borrow_book()

    library.borrow_book("9780439708180")

    # Assert: check that the book's is_borrowed is now True
    assert book.is_borrowed is True

def test_borrow_book_with_already_borrowed_raises_error():
    # Arrange: set up a new library, add one book, and borrow it once so it becomes already borrowed
    library = Library()

    book = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997, "9780439708180")
    library.add_book(book)

    library.borrow_book("9780439708180")

    # Act & Assert: try to borrow the same book again, expect a ValueError to be raised
    with pytest.raises(ValueError):
        library.borrow_book("9780439708180")

def test_borrow_book_with_missing_isbn_raises_error():
    # Arrange: set up a new library (it can be empty, or have books with different ISBNs)
    library = Library()
    book = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997, "9780439708180")
    library.add_book(book)

    # Act & Assert: try to borrow a book using an ISBN that doesn't exist, expect a ValueError to be raised
    with pytest.raises(ValueError):
        library.borrow_book("9780439708182")