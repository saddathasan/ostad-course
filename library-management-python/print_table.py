def print_as_table(books):
    # Custom function to display books in a tabular format
    headers = ["Title", "Authors", "ISBN", "Year", "Price", "Quantity"]
    print("{:<30} {:<20} {:<15} {:<10} {:<10} {:<10}".format(*headers))
    print("-" * 100)
    for book in books:
        print("{:<30} {:<20} {:<15} {:<10} {:<10} {:<10}".format(
            book["Title"], book["Authors"], book["ISBN"], book["Year"], book["Price"], book["Quantity"]
        ))
