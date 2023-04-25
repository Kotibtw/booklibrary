print("Welcome to library management system")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            self.borrowed_books.append(book)
            book.is_borrowed = True
            print(f"{self.name} has borrowed {book.title} by {book.author.name}.")
        else:
            print(f"{book.title} by {book.author.name} is already borrowed.")

    def return_book(self, book):
        if book.is_borrowed and book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False
            print(f"{self.name} has returned {book.title} by {book.author.name}.")
        else:
            print(f"{self.name} did not borrow {book.title} by {book.author.name}.")

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.authors = {}

    def add_item(self, book):
        author_name = book.author.name
        if author_name not in self.authors:
            self.authors[author_name] = Author(author_name)
        self.authors[author_name].add_book(book)
        self.books.append(book)
        print(f"{book.title} by {book.author.name} has been added to the library.")

    def add_member(self, member):
        self.members.append(member)
        print(f"{member.name} was successfully added to the system.")

    def remove_member(self, member_name):
        for member in self.members:
            if member.name == member_name:
                self.members.remove(member)
                print(f"{member.name} was successfully removed from the system.")
                break
        else:
            print("Member not found.")

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                author_name = book.author.name
                self.authors[author_name].books.remove(book)
                self.books.remove(book)
                print(f"{book.title} by {book.author.name} has been removed from the library.")
                break
        else:
            print("Book not found.")

    def list_members(self):
        print("Members:")
        for member in self.members:
            print(f"- {member.name}")

    def list_books(self):
        print("Books:")
        for book in self.books:
            status = "Available" if not book.is_borrowed else "Borrowed"
            print(f"- {book.title} by {book.author.name} ({status})")

    def list_borrowed_books(self, member_name):
        for member in self.members:
            if member.name == member_name:
                if len(member.borrowed_books) == 0:
                    print(f"{member.name} has not borrowed any books.")
                else:
                    print(f"{member.name} has borrowed the following books:")
                    for book in member.borrowed_books:
                        print(f"- {book.title} by {book.author.name}")
                break
        else:
            print("Member not found.")
def menu(library):
    while True:
        print("1. Add book")
        print("2. Remove book")
        print("3. List books")
        print("4. Add member")
        print("5. Remove member")
        print("6. List members")
        print("7. Borrow book")
        print("8. Return book")
        print("9. List borrowed books")
        print("10. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            
            title = input("Enter a books title: ")
            author = input("Enter a book author: ")
            book = Book(title, Author(author))
            library.add_item(book)
            
        elif choice == "2":
            
            book_id = input("Enter a book title: ")
            library.remove_book(book_id)
            
        elif choice == "3":
            
            library.list_books()
            
        elif choice == "4":
            
            name = input("Enter a name to be a member: ")
            member = Member(name)
            library.add_member(member)
            
        elif choice == "5":
            
            member_id = input("Enter a member name: ")
            library.remove_member(member_id)
            
        elif choice == "6":
            
            library.list_members()
            
        elif choice == "7":
            
            book_id = input("Enter a book title: ")
            member_id = input("Enter a member name: ")
            
            book = None
            for b in library.books:
                if b.title == book_id:
                    book = b
                    break
            else:
                print("The book didn't exist.")
                continue
            
            member = None
            for m in library.members:
                if m.name == member_id:
                    member = m
                    break
            else:
                print("The member didn't exist.")
                continue
            
            if book.is_borrowed:
                print("The book is already borrowed.")
            else:
                member.borrow_book(book)
                print("the book has been borrowed.")
                
        elif choice == "8":
            
            book_id = input("Enter a book title: ")
            member_id = input("Enter a member name: ")
            
            book = None
            for b in library.books:
                if b.title == book_id:
                    book = b
                    break
            else:
                print("The book didn't exist.")
                continue
            
            member = None
            for m in library.members:
                if m.name == member_id:
                    member = m
                    break
            else:
                print("The member didn't exist.")
                continue
            
            if not book.is_borrowed or book not in member.borrowed_books:
                print("The book cann't be returned.")
            else:
                member.return_book(book)
                print("The book has been returned.")
                
        elif choice == "9":
            
            member_id = input("Enter a member name: ")
            library.list_borrowed_books(member_id)
            
        elif choice == "10":
            
            print("See you later!")
            break
        else:
            print("Invalid choice. Please enter a number from 1-10.")

my_library = Library()
menu(my_library)

