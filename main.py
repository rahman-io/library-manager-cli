from library import Library
from book import Book

def main():
    library = Library()

    try:
        library.load_books("books.json")
    except FileNotFoundError:
        pass

    while True:
        print("1. Add book")
        print("2. Remove book")
        print("3. Search book")
        print("4. List all books")
        print("5. Borrow book")
        print("6. Save and exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            isbn = input("ISBN: ")

            try:
                book = Book(title, author, int(year), isbn)
                library.add_book(book)
                print("Book added successfully.")
            except ValueError as e:
                print(e)

        elif choice == "2":
            isbn = input("ISBN to remove: ")

            try:
                library.remove_book(isbn)
                print("Book removed successfully.")
            except ValueError as e:
                print(e)

        elif choice == "3":
            keyword = input("Search keyword: ")
            results = library.search_book(keyword)

            if not results:
                print("No books found.")
            else:
                for b in results:
                    print(b.display_info())

        elif choice == "4":
            if not library.books:
                print("No books in the library.")
            else:
                for i, b in enumerate(reversed(library.books), start=1):
                    print(f"{i}. {b.display_info()}")

        elif choice == "5":
            isbn = input("ISBN to borrow: ")

            try:
                library.borrow_book(isbn)
                print("Book borrowed successfully.")
            except ValueError as e:
                print(e)

        elif choice == "6":
            library.save_books("books.json")
            print(f"{len(library.books)} book(s) saved. See you next time!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()

