import loan_handler
from print_table import print_loan_table
from datetime import datetime

loan_file = "loans.csv"

def view_loans():
    loans = loan_handler.load_loans(loan_file)
    if not loans:
        print("No loan records available.")
    else:
        # Mark overdue loans
        current_date = datetime.now()
        for loan in loans:
            due_date = datetime.strptime(loan["DueDate"], "%Y-%m-%d")
            loan["Overdue"] = "Yes" if current_date > due_date else "No"
        
        print("\nLoan Records:")
        print_loan_table(loans)
