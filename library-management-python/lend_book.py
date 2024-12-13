import save_books_to_file
import loan_handler
from datetime import datetime, timedelta

book_file = "books.csv"
loan_file = "loans.csv"

def lend_book(title, borrower_name, borrower_phone):
    books = save_books_to_file.load_books_from_csv(book_file)
    loans = loan_handler.load_loans(loan_file)
    
    for book in books:
        if book["Title"].lower() == title.lower():
            if int(book["Quantity"]) > 0:
                # Update book quantity
                book["Quantity"] = str(int(book["Quantity"]) - 1)
                
                # Create loan record
                borrow_date = datetime.now()
                due_date = borrow_date + timedelta(days=14)
                loan = {
                    "Title": title,
                    "Borrower": borrower_name,
                    "Phone": borrower_phone,
                    "BorrowDate": borrow_date.strftime("%Y-%m-%d"),
                    "DueDate": due_date.strftime("%Y-%m-%d")
                }
                loans.append(loan)
                
                # Save updates
                save_books_to_file.save_books_to_csv(book_file, books)
                loan_handler.save_loans(loan_file, loans)
                
                print(f"The book '{title}' has been lent to {borrower_name}. Due date: {due_date.strftime('%Y-%m-%d')}")
                return
            else:
                print("There are not enough books available to lend.")
                return
    print("Book not found in the library.")
