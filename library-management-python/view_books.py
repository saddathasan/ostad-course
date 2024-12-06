import save_books_to_file
from print_table import print_as_table

file_name = "books.csv"  # File to store book information

def view_books():
    books = save_books_to_file.load_books_from_csv(file_name)
    if not books:
        print("No books available.")
    else:
        print("\nBooks in the Library:")
        print_as_table(books)
