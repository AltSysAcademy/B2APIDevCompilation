from library_system import Book, Library

book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

school_library = Library()
school_library.add_book(book1)
school_library.add_book(book2)

school_library.show_books()