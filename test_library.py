import unittest
from library import Library, Book

class TestLibrary(unittest.TestCase):
    def test_add_book(self):
        library = Library()
        book = Book("1", "Test Book", "Author Name", 2024)
        library.add_book(book)
        self.assertIn(book, library.books)
    
    def test_borrow_book(self):
        library = Library()
        book = Book("1", "Test Book", "Author Name", 2024)
        library.add_book(book)
        library.borrow_book("1")
        self.assertFalse(book.available)
    
    def test_return_book(self):
        library = Library()
        book = Book("1", "Test Book", "Author Name", 2024)
        library.add_book(book)
        library.borrow_book("1")
        library.return_book("1")
        self.assertTrue(book.available)
    
    def test_available_books(self):
        library = Library()
        book1 = Book("1", "Test Book 1", "Author Name", 2024)
        book2 = Book("2", "Test Book 2", "Another Author", 2023)
        library.add_book(book1)
        library.add_book(book2)
        library.borrow_book("1")
        available_books = library.view_available_books()
        self.assertIn(book2, available_books)
        self.assertNotIn(book1, available_books)

    
    


if __name__ == '__main__':
    unittest.main()
