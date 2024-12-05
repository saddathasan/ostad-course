def validate_name(name):
    if not name.isalpha():
        raise ValueError("Name must only contain alphabetic characters.")

def validate_phone(phone):
    if not phone.isdigit():
        raise ValueError("Phone number must only contain digits.")

def validate_email(email):
    if "@" not in email or "." not in email:
        raise ValueError("Invalid email format.")
