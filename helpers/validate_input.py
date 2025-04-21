from utils.exceptions import InvalidInputException

def validate_email(email, error_message="formate de email invalido."):
    import re
    regex = r'^\S+@\S+\.\S+$'
    if re.search(regex, email):
        return True
    raise InvalidInputException(error_message)

def validate_input(value, expected_type, error_message="tipo de dato invalido."):
    if isinstance(value, expected_type):
        return True
    raise InvalidInputException(error_message)
