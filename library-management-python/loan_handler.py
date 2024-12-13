import csv

def load_loans(file_name):
    loans = []
    try:
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                loans.append(row)
    except FileNotFoundError:
        pass
    return loans

def save_loans(file_name, loans):
    with open(file_name, "w", newline="") as file:
        fieldnames = ["Title", "Borrower", "Phone", "BorrowDate", "DueDate"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(loans)
