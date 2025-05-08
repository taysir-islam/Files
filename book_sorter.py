books = [
    {"title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams", "isbn": "978-0345391803"},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "isbn": "978-0141439518"},
    {"title": "1984", "author": "George Orwell", "isbn": "978-0451524935"},
]

books.sort(key=lambda x: x["title"])
print(books)

books.sort(key=lambda book: book["author"])
print("\nSorted by author:", books)

books.sort(key=lambda book: book["isbn"].replace("-", ""))  
print("\nSorted by ISBN:", books)


sorted_by_title = sorted(books, key=lambda book: book["title"])
print("\nNew list sorted by title (original unchanged):", sorted_by_title)
print("Original list:", books)