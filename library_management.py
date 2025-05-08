import datetime

class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
    
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nAvailable: {self.is_available}"

class Member:
    def __init__(self,member_id,name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
        
    def __str__(self):
        return f"Member ID: {self.member_id}\nName: {self.name}\nBorrowed Books: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = {}  
        self.members = {}   
        
    def add_book(self, book):
        if book.isbn not in self.books:
            self.books[book.isbn] = book
            print(f"Book '{book.title}' added successfully.")
        else:
            print("Book with this ISBN already exists.")
            
    def add_member(self, member):
        if member.member_id not in self.members:
            self.members[member.member_id] = member
            print(f"Member '{member.name}' added successfully.")
        else:
            print("Member with this ID already exists.")

    def borrow_book(self, member_id, isbn):
        if member_id in self.members and isbn in self.books:
            member = self.members[member_id]
            book = self.books[isbn]
            if book.is_available:
                book.is_available = False
                member.borrowed_books.append(book)
                print(f"'{book.title}' borrowed by '{member.name}'.")
            else:
                print(f"'{book.title}' is currently unavailable.")
        else:
            print("Invalid member ID or ISBN.")

    def return_book(self, member_id, isbn):
         if member_id in self.members and isbn in self.books:
            member = self.members[member_id]
            book = self.books[isbn]
            if book in member.borrowed_books:
                book.is_available = True
                member.borrowed_books.remove(book)
                print(f"'{book.title}' returned by '{member.name}'.")
            else:
                print(f"'{book.title}' was not borrowed by this member.")
         else:
            print("Invalid member ID or ISBN.")

    def display_available_books(self):
        print("\nAvailable Books:")
        for book in self.books.values():
            if book.is_available:
                print(book)
                print("-" * 20)

    def display_borrowed_books(self, member_id):
         if member_id in self.members:
            member = self.members[member_id]
            print(f"\nBooks borrowed by {member.name}:")
            if member.borrowed_books:
                for book in member.borrowed_books:
                    print(book)
                    print("-" * 20)
            else:
                print("No books borrowed.")
         else:
            print("Invalid member ID.")        
            
library = Library()

book1 = Book(input("Enter the title of the book: "), input("Enter the author of the book: "), input("Enter the ISBN of the book: "))
book2 = Book(input("Enter the title of the book: "), input("Enter the author of the book: "), input("Enter the ISBN of the book: "))
library.add_book(book1)
library.add_book(book2)

print("-" * 20)

member1 = Member("9210", "Alice Smith")
member2 = Member("4235", "Bob Johnson")
library.add_member(member1)
library.add_member(member2)

print("-" * 20)

library.borrow_book(input("Enter the member ID: "), input("Enter the ISBN of wanted book: "))
library.borrow_book(input("Enter the member ID: "), input("Enter the ISBN of wanted book: "))

print("-" * 20)

library.return_book(input("Enter the member ID: "), input("Enter the ISBN of the book to return: "))
library.return_book(input("Enter the member ID: "), input("Enter the ISBN of the book to return: "))

print("-" * 20)

library.display_available_books()

print("-" * 20)

library.display_borrowed_books("9210")
library.display_borrowed_books("4235") 

print("-" * 20)
