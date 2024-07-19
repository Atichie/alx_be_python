class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page count: {self.page_count}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)
        
name = '_main_'
if name == "_main_":
    try:
        my_library = Library()

        book1 = Book("Pride and Prejudice", "Jane Austen")
        ebook1 = EBook("Snow Crash", "Neal Stephenson", 500)
        printbook1 = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

        my_library.add_book(book1)
        my_library.add_book(ebook1)
        my_library.add_book(printbook1)

        my_library.list_books()
    except Exception as e:
        print(f"An expected error occurred: {e}", file=sys.stderr)




