class Book: 
    def __init__(self, title, author):
        self.title = title
        self.author = author 
        self.is_checked_out = False
    
    def borrow(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"You have borrowed '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is already out.")

    def return_book(self): 
        self.is_checked_out = False
        print(f"You have successfully returned '{self.title}'.")

class Library:
    def __init__(self):
        self.books = [] 
    
    def add_book(self, book):
        self.books.append(book)

    def show_available_books(self):
        print("\nAvailable books:")
        for book in self.books:

            if not book.is_checked_out:
                print(f"- {book.title} by {book.author}")


class DigitalBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    def borrow(self):
        print(f"Downloading '{self.title}' ({self.file_size})... Done! ")

class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    
    def take_book(self, book):
        if not book.is_checked_out:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"Hey {self.name}, {book.title} isn't available right now.")
    
    def list_my_books(self):
        print(f"\n{self.name}'s Collection:")
        for book in self.borrowed_books:
            print(f"- {book.title}")

    def return_item(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.removed(book)
        else:
            print(f"Wait, {self.name}, you don't have {book.title}")




my_city_library = Library()

book1 = Book("The Hobbit", "J.R.R. Tolkien")
book2 = Book("1984", "George Orwell") 

my_city_library.add_book(book1)
my_city_library.add_book(book2)

# Test borrowing
book1.borrow()

# Test showing available
my_city_library.show_available_books()

physical = Book("The hobbit", "Tolkien")
digital = DigitalBook("Python 101", "Guido", "5MB")

library_items = [physical, digital]
for item in library_items:
    item.borrow()

# Create the actors
my_library = Library()  
me = User("Alex")
hp = Book("Harry Potter", "J.K. Rowling")

# Add book to library
my_library.add_book(hp)

# User interacts with the book
me.take_book(hp)

# Check the user's status
me.list_my_books()

