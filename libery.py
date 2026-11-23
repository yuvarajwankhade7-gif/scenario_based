# Book class
class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
        self.category = self.categorize_book()

    def categorize_book(self):
        # Categorize based on price
        if self.price >= 500:
            return "Premium"
        else:
            return "Standard"

    def display_info(self):
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, "
              f"Price: {self.price}, Category: {self.category}")


# Library class
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully!")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\n--- Library Books ---")
            for book in self.books:
                book.display_info()


# Example usage
if __name__ == "__main__":
    library = Library()

    # Adding books
    book1 = Book(1, "Python Basics", "John Doe", 450)
    book2 = Book(2, "Advanced Python", "Jane Smith", 750)

    library.add_book(book1)
    library.add_book(book2)

    # Display all books
    library.display_books()
