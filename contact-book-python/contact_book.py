import contact_operations as ops
import utils

def display_menu():
    print("\nContact Book Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Remove Contact")
    print("4. Search Contact")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            try:
                name = input("Enter name: ")
                utils.validate_name(name)
                email = input("Enter email: ")
                utils.validate_email(email)
                phone = input("Enter phone number: ")
                utils.validate_phone(phone)
                address = input("Enter address: ")
                ops.add_contact(name, email, phone, address)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            ops.view_contacts()
        elif choice == "3":
            phone = input("Enter the phone number of the contact to remove: ")
            ops.remove_contact(phone)
        elif choice == "4":
            query = input("Enter name, email, or phone number to search: ")
            ops.search_contact(query)
        elif choice == "5":
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
