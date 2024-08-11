import unittest
from library import Library, Book

class TestLibrary(unittest.TestCase):
    def test_add_book(self):
        library = Library()
        book = Book("12345", "Test Book", "Author Name", 2024)
        library.add_book(book)
        self.assertIn(book, library.books)

if __name__ == '__main__':
    unittest.main()
