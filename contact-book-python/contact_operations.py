import file_handler
import utils

file_name = "contacts.csv"  # CSV file to store all contact information


def add_contact(name, email, phone, address):
    contacts = file_handler.load_contacts_from_csv(file_name)

    # Check for duplicate phone number
    for contact in contacts:
        if contact["Phone"] == phone:
            print("\nThis phone number is already in use.")
            print(
                f"Name: {contact['Name']}, Email: {contact['Email']}, Phone: {contact['Phone']}, Address: {contact['Address']}")
            return False

    # Add new contact
    new_contact = {"Name": name, "Email": email, "Phone": phone, "Address": address}
    contacts.append(new_contact)
    file_handler.save_contacts_to_csv(file_name, contacts)
    print("Contact added successfully!")
    return True


def view_contacts():
    contacts = file_handler.load_contacts_from_csv(file_name)
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContacts:")
        print_as_table(contacts)


def remove_contact(phone):
    contacts = file_handler.load_contacts_from_csv(file_name)
    updated_contacts = [contact for contact in contacts if contact["Phone"] != phone]

    if len(contacts) == len(updated_contacts):
        print("Error: Contact not found.")
    else:
        file_handler.save_contacts_to_csv(file_name, updated_contacts)
        print("Contact removed successfully!")


def search_contact(query):
    contacts = file_handler.load_contacts_from_csv(file_name)
    found = False
    for contact in contacts:
        if query.lower() in contact["Name"].lower() or query.lower() in contact["Email"].lower() or query == contact[
            "Phone"]:
            print(
                f"Found Contact - Name: {contact['Name']}, Email: {contact['Email']}, Phone: {contact['Phone']}, Address: {contact['Address']}")
            found = True
    if not found:
        print("No contact found with the given details.")


def print_as_table(contacts):
    # Custom function to display contacts in a tabular format
    headers = ["Name", "Email", "Phone", "Address"]
    print("{:<20} {:<30} {:<15} {:<30}".format(*headers))
    print("-" * 95)
    for contact in contacts:
        print("{:<20} {:<30} {:<15} {:<30}".format(
            contact["Name"], contact["Email"], contact["Phone"], contact["Address"]
        ))
