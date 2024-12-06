import add_book
import view_books
import utils

def display_menu():
    print("\nLibrary Management System")
    print("0. Exit")
    print("1. Add Book")
    print("2. View All Books")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "0":
            print("Exiting the Library Management System. Goodbye!")
            break
        elif choice == "1":
            try:
                title = input("Enter the book title: ")
                authors = input("Enter the author's name: ")
                isbn = input("Enter the ISBN: ")
                year = input("Enter the publishing year: ")
                utils.validate_positive_integer(year, "Publishing Year")
                price = input("Enter the price: ")
                utils.validate_positive_float(price, "Price")
                quantity = input("Enter the quantity: ")
                utils.validate_positive_integer(quantity, "Quantity")
                add_book.add_book(title, authors, isbn, year, price, quantity)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            view_books.view_books()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
