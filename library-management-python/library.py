import add_book
import view_books
import lend_book
import return_book
import view_loans
import utils

def display_menu():
    print("\nLibrary Management System")
    print("0. Exit")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Lend Book")
    print("4. Return Book")
    print("5. View Loan Records")

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
                authors = input("Enter the authors (comma-separated): ")
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
        elif choice == "3":
            title = input("Enter the book title to lend: ")
            borrower_name = input("Enter the borrower's name: ")
            borrower_phone = input("Enter the borrower's phone number: ")
            lend_book.lend_book(title, borrower_name, borrower_phone)
        elif choice == "4":
            title = input("Enter the book title to return: ")
            borrower_phone = input("Enter the borrower's phone number: ")
            return_book.return_book(title, borrower_phone)
        elif choice == "5":
            view_loans.view_loans()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
