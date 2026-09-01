# library-manager-cli

A command-line library management system built in Python, developed with a
test-first (shift-left) workflow using pytest.

## Features

- Add, remove, and search books by title or author
- List all books, newest addition shown first
- Persist the library to JSON and reload it on startup
- Input validation with clear error handling (`TypeError`, `ValueError`)
- Polymorphic `Book` / `EBook` model via inheritance

## Tech stack

- Python 3.14
- pytest for unit testing
- JSON for lightweight data persistence

## Running the app

\```bash
python main.py
\```

## Running the tests

\```bash
pytest
\```

## Project structure

- `book.py` — `Book` and `EBook` classes (OOP core)
- `library.py` — `Library` class: add/remove/search/save/load
- `main.py` — CLI menu loop
- `test_library.py` — pytest suite covering `Library` behavior

## Status

Actively developed as a portfolio project. Known issues and planned
enhancements are tracked on the project's Jira board.