def print_as_table(books):
    # Tabular display for books with word wrapping for long text
    headers = ["Title", "Authors", "ISBN", "Year", "Price", "Quantity"]
    column_widths = [30, 20, 15, 10, 10, 10]
    
    # Print header row with separator
    print_row(headers, column_widths)
    print_separator(column_widths)
    
    # Print each book record with wrapping
    for book in books:
        row = [
            book["Title"],
            book["Authors"],
            book["ISBN"],
            book["Year"],
            f"${float(book['Price']):.2f}",  # Format price as currency
            book["Quantity"]
        ]
        wrapped_rows = wrap_row(row, column_widths)
        for wrapped_row in wrapped_rows:
            print_row(wrapped_row, column_widths)
        print_separator(column_widths)


def print_loan_table(loans):
    # Tabular display for loans with word wrapping for long text
    headers = ["Title", "Borrower", "Phone", "BorrowDate", "DueDate", "Overdue"]
    column_widths = [30, 20, 15, 12, 12, 8]
    
    # Print header row with separator
    print_row(headers, column_widths)
    print_separator(column_widths)
    
    # Print each loan record with wrapping
    for loan in loans:
        row = [
            loan["Title"],
            loan["Borrower"],
            loan["Phone"],
            loan["BorrowDate"],
            loan["DueDate"],
            loan["Overdue"]
        ]
        wrapped_rows = wrap_row(row, column_widths)
        for wrapped_row in wrapped_rows:
            print_row(wrapped_row, column_widths)
        print_separator(column_widths)


def wrap_row(row, column_widths):
    """
    Wraps each cell in the row to fit within its respective column width.
    Returns a list of rows with wrapped content.
    """
    # Split each cell into lines based on column width
    wrapped_cells = [
        wrap_text(cell, width) for cell, width in zip(row, column_widths)
    ]
    
    # Determine the maximum number of lines in any cell
    max_lines = max(len(cell_lines) for cell_lines in wrapped_cells)
    
    # Create rows with wrapped content, line by line
    wrapped_rows = []
    for i in range(max_lines):
        wrapped_rows.append([
            wrapped_cells[col][i] if i < len(wrapped_cells[col]) else ""
            for col in range(len(column_widths))
        ])
    return wrapped_rows


def wrap_text(text, width):
    """
    Wraps a single cell's text to fit within the specified width.
    Returns a list of lines.
    """
    if len(text) <= width:
        return [text]
    # Split the text into multiple lines
    lines = []
    while len(text) > width:
        space_index = text.rfind(" ", 0, width)
        if space_index == -1:  # No space found, force break
            lines.append(text[:width])
            text = text[width:]
        else:  # Break at the last space within the width
            lines.append(text[:space_index])
            text = text[space_index + 1:]
    lines.append(text)
    return lines


def print_row(row, column_widths):
    """
    Prints a single row with properly formatted columns.
    """
    formatted_row = " | ".join(f"{item:<{width}}" for item, width in zip(row, column_widths))
    print(f"| {formatted_row} |")


def print_separator(column_widths):
    """
    Prints a separator row based on column widths.
    """
    separator = "-+-".join("-" * width for width in column_widths)
    print(f"+-{separator}-+")
