import csv

def load_contacts_from_csv(file_name):
    contacts = []
    try:
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        pass  # If file doesn't exist, return an empty list
    return contacts

def save_contacts_to_csv(file_name, contacts):
    with open(file_name, "w", newline="") as file:
        fieldnames = ["Name", "Email", "Phone", "Address"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)
