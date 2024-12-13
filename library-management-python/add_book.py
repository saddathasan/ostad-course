import save_books_to_file

file_name = "books.csv"

def add_book(title, authors, isbn, year, price, quantity):
    books = save_books_to_file.load_books_from_csv(file_name)
    
    new_book = {
        "Title": title,
        "Authors": authors,
        "ISBN": isbn,
        "Year": year,
        "Price": price,
        "Quantity": quantity
    }
    books.append(new_book)
    save_books_to_file.save_books_to_csv(file_name, books)
    print("Book added successfully!")
