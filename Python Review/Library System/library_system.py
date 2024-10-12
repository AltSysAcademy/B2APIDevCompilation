# Library - is a collection of books (Object)
# Book - title, author (Object)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def get_details(self):
        return f"{self.title} - {self.author}"
    

class Library:
    def __init__(self):
        self.books = []
    
    # Add a book
    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book.title} - {book.author} to library.")
    
    # Show all books
    def show_books(self):
        if len(self.books) > 0:
            print("Available Books:")
            for book in self.books:
                print(book.get_details())
        else:
            print("No books stored.")