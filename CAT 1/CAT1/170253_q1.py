
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"The book '{self.title}' has been borrowed.")
        else:
            print(f"The book '{self.title}' is already borrowed.")

    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"The book '{self.title}' has been returned.")
        else:
            print(f"The book '{self.title}' was not borrowed.")

class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
        else:
            print(f"Sorry, '{book.title}' is currently unavailable.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
        else:
            print(f"You don't have the book '{book.title}' borrowed.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{self.name} has no borrowed books.")

# Sample functionality
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class LibraryMember:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            print(f"Borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"Returned '{book.title}'")
        else:
            print(f"'{book.title}' is not in your borrowed books.")

library_books = [
    Book("Nearly all Men in Lagos Are Mad", "Damilare Kuku"),
    Book("Rich Dad Poor Dad", "Robert T. Kiyosaki and Sharon Lechter"),
    Book("Newly Wed", "Mansi Choksi")
]

member = LibraryMember("Alice")

def library_system():
    while True:
        choice = input("\nOptions: 1) Borrow 2) Return 3) List 4) Exit: ")
        if choice == "1":
            for i, book in enumerate(library_books):
                if not book.is_borrowed:
                    print(f"{i + 1}) {book.title}")
            book_idx = int(input("Select book: ")) - 1
            if 0 <= book_idx < len(library_books):
                member.borrow_book(library_books[book_idx])
        elif choice == "2":
            for i, book in enumerate(member.borrowed_books):
                print(f"{i + 1}) {book.title}")
            book_idx = int(input("Select book: ")) - 1
            if 0 <= book_idx < len(member.borrowed_books):
                member.return_book(member.borrowed_books[book_idx])
        elif choice == "3":
            for book in member.borrowed_books:
                print(f"- {book.title}")
        elif choice == "4":
            break


