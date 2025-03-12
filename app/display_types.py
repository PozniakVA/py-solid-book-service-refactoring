from app.interfaces import DisplayBookInterface
from app.main import Book


class ConsoleDisplay(DisplayBookInterface):
    def display_book(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayBookInterface):
    def display_book(self, book: Book) -> None:
        print(book.content[::-1])
