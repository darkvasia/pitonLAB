class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author}, {self.year}"

def log_activity(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__} was called")
        return result
    return wrapper

class Librarian:
    def __init__(self):
        self.books = []

    @log_activity
    def add_book(self, book):
        self.books.append(book)
        return f"Book '{book}' added."

    @log_activity
    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return f"Book '{title}' removed."
        return f"Book '{title}' not found."

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

class Library:
    def __init__(self):
        self.librarian = Librarian()

    def load_books(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                title, author, year = line.strip().split(',')
                self.librarian.add_book(Book(title, author, year))

    def save_books(self, filename):
        with open(filename, 'w') as file:
            for book in self.librarian.books:
                file.write(f"{book.title},{book.author},{book.year}\n")


library = Library()
library.librarian.add_book(Book("New Book", "Author Name", 2024))
library.save_books("books.txt")
library.load_books("books.txt")