class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"Book '{self.title}' has been borrowed.")
        else:
            print(f"Book '{self.title}' is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"Book '{self.title}' has been returned.")
        else:
            print(f"Book '{self.title}' was not borrowed.")


class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_borrowed:
            print(f"Cannot borrow '{book.title}'; it's already borrowed.")
        else:
            book.borrow()
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed '{book.title}'.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name} does not have '{book.title}' borrowed.")


class Library:
    def __init__(self):
        self.books = {}      # Key: ISBN, Value: Book instance
        self.patrons = {}    # Key: Patron ID, Value: Patron instance

    def add_book(self, book):
        if book.isbn in self.books:
            print(f"Book with ISBN {book.isbn} already exists.")
        else:
            self.books[book.isbn] = book
            print(f"Book '{book.title}' added to the library.")

    def register_patron(self, patron):
        if patron.patron_id in self.patrons:
            print(f"Patron ID {patron.patron_id} already registered.")
        else:
            self.patrons[patron.patron_id] = patron
            print(f"Patron '{patron.name}' registered with ID {patron.patron_id}.")

    def borrow_book(self, patron_id, isbn):
        if patron_id not in self.patrons:
            print(f"Patron ID {patron_id} not found.")
            return
        if isbn not in self.books:
            print(f"Book with ISBN {isbn} not found.")
            return

        patron = self.patrons[patron_id]
        book = self.books[isbn]
        patron.borrow_book(book)

    def return_book(self, patron_id, isbn):
        if patron_id not in self.patrons:
            print(f"Patron ID {patron_id} not found.")
            return
        if isbn not in self.books:
            print(f"Book with ISBN {isbn} not found.")
            return

        patron = self.patrons[patron_id]
        book = self.books[isbn]
        patron.return_book(book)


# Example Usage:
if __name__ == "__main__":
    # Initialize library
    library = Library()

    # Add books
    book1 = Book("1984", "George Orwell", "1234567890")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")
    library.add_book(book1)
    library.add_book(book2)

    # Register patrons
    patron1 = Patron("Alice Smith", "P001")
    patron2 = Patron("Bob Johnson", "P002")
    library.register_patron(patron1)
    library.register_patron(patron2)

    # Borrow and return books
    library.borrow_book("P001", "1234567890")  # Alice borrows "1984"
    library.borrow_book("P002", "1234567890")  # Bob tries to borrow "1984"
    library.return_book("P001", "1234567890")  # Alice returns "1984"
    library.borrow_book("P002", "1234567890")  # Bob borrows "1984"
