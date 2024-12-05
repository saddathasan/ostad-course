from add_contact import add_contact

def option_handler(args):
    if args == "1":
        add_contact()
    elif args == "2":
        print("you wanted to view all contacts")
    elif args == "3":
        print("you wanted to search for a contact")
    elif args == "4":
        print("you wanted to delete a contact")
    elif args == "0":
        print("you wanted to exit")
        return True
    else:
        print("\nInvalid choice. Please try again.\n")