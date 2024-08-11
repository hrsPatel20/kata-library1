class Book:
    def __init__(self, id, title, author, year):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
    
    def borrow_book(self, id):
        for book in self.books:
            if book.id == id and book.available:
                book.available = False
                return
        raise ValueError("Book is not available")
    
    def return_book(self, id):
        for book in self.books:
            if book.id == id:
                book.available = True
                return
        raise ValueError("Book not found")

    def view_available_books(self):
        return [book for book in self.books if book.available]
    


