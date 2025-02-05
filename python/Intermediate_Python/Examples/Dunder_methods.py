class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

    def __add__(self, other):
        if isinstance(other, Book):
            return Book(f"{self.title} & {other.title}", self.author, self.pages + other.pages)
        return NotImplemented

# Usage
book1 = Book("1984", "George Orwell", 328)
book2 = Book("Animal Farm", "George Orwell", 112)
book3 = Book("1984", "George Orwell", 328)

print(book1)              # Output: '1984' by George Orwell
print(repr(book1))        # Output: Book(title='1984', author='George Orwell', pages=328)
print(len(book1))         # Output: 328
print(book1 == book3)     # Output: True
print(book1 == book2)     # Output: False

combined_book = book1 + book2
print(combined_book)      # Output: '1984 & Animal Farm' by George Orwell
print(len(combined_book)) # Output: 440