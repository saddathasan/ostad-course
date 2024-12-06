def validate_positive_integer(value, field_name):
    if not value.isdigit() or int(value) <= 0:
        raise ValueError(f"{field_name} must be a positive integer.")

def validate_positive_float(value, field_name):
    try:
        val = float(value)
        if val <= 0:
            raise ValueError(f"{field_name} must be a positive number.")
    except ValueError:
        raise ValueError(f"{field_name} must be a positive number.")
