import save_books_to_file
import loan_handler

book_file = "books.csv"
loan_file = "loans.csv"

def return_book(title, borrower_phone):
    books = save_books_to_file.load_books_from_csv(book_file)
    loans = loan_handler.load_loans(loan_file)
    
    for loan in loans:
        if loan["Title"].lower() == title.lower() and loan["Phone"] == borrower_phone:
            # Remove loan record
            loans.remove(loan)
            
            # Update book quantity
            for book in books:
                if book["Title"].lower() == title.lower():
                    book["Quantity"] = str(int(book["Quantity"]) + 1)
                    break
            
            # Save updates
            save_books_to_file.save_books_to_csv(book_file, books)
            loan_handler.save_loans(loan_file, loans)
            
            print(f"The book '{title}' has been returned. Thank you!")
            return
    print("No matching loan record found.")
