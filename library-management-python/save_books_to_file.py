import csv

def load_books_from_csv(file_name):
    books = []
    try:
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                books.append(row)
    except FileNotFoundError:
        pass  # If file doesn't exist, return an empty list
    return books

def save_books_to_csv(file_name, books):
    with open(file_name, "w", newline="") as file:
        fieldnames = ["Title", "Authors", "ISBN", "Year", "Price", "Quantity"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)
