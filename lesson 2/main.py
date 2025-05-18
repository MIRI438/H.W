import unittest
from library import Library
from book import Book

class TestLibrary(unittest.TestCase):

    def test_add_book(self):
        library = Library()
        new_book = Book("Emuna", "Haim")

        library.add_book(new_book)
        self.assertIn(new_book,library.books)

    def test_add_user(self):
        library = Library()
        with self.assertRaises(ValueError):
            library.add_user(None)

    def test_check_out_book(self):
        library = Library()
        with self.assertRaises(ValueError):
            library.check_out_book(username="bhj",book="ajg")

    def test_return_book(self):
        library = Library()
        with self.assertRaises(ValueError):
            library.return_book(username="bhj",book="ajg")

    def test_search_book(self):
        library = Library()
        result = library.search_books("vdf")  
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()