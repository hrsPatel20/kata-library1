class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
    
    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.available:
                book.available = False
                return
        raise ValueError("Book is not available")
