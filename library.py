class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

    def display_info(self):
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Copies Available: {self.copies}")

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book_id, title, author, copies):
        new_book = Book(book_id, title, author, copies)
        self.books.append(new_book)
        print("Book added Successfully.")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Books in library: ")
            for book in self.books:
                book.display_info()

    def search_book(self, title):
        found = False
        for book in self.books:
            if book.title.lower() == title.lower():
                book.display_info()
                found = True
                break
        if not found:
            print("Book not found!!")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.copies > 0:
                    book.copies -= 1
                    print("Book borrowed Successfully.")
                else:
                    print("Book is not available")
                return
        print("Book NOT found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.copies += 1
                print("Book returned Successfully.")
                return
        print("Book Not found.")

# ===== Main Menu =====
library = Library()

while True:
    print("\n==== Library Management System ====")
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. !!! EXIT !!!")

    choice = input("Enter Your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter book author: ")
        copies = int(input("Enter number of Copies: "))
        library.add_book(book_id, title, author, copies)

    elif choice == '2':
        library.display_books()

    elif choice == '3':
        title = input("Enter book title to search: ")
        library.search_book(title)

    elif choice == '4':
        title = input("Enter book title to borrow: ")
        library.borrow_book(title)

    elif choice == '5':
        title = input("Enter book title to return: ")
        library.return_book(title)

    elif choice == '6':
        print("Exiting Program. Goodbye!!")
        break
    else:
        print("Invalid choice. Please try again.")
