# utils/exceptions.py

""" Arhcivo de excepciones para el manejo de errores en la aplicacion """

# Exceptions para controllers y services 
class BusinessLogicException(Exception):
    status_code = 500

    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.message = message
        if status_code:
            self.status_code = status_code

class NotFoundException(BusinessLogicException):
    status_code = 404

    def __init__(self, message="Resource not found"):
        super().__init__(message)
        self.message = message

class InvalidInputException(BusinessLogicException):
    status_code = 400

    def __init__(self, message="Invalid input provided"):
        super().__init__(message)
        self.message = message

class AlreadyExistsException(BusinessLogicException):
    status_code = 409

    def __init__(self, message="Resource already exists"):
        super().__init__(message)
        self.message = message

class NotFoundException(BusinessLogicException):
    status_code = 404

    def __init__(self, message="Resource not found"):
        super().__init__(message)
        self.message = message

class UnresolvedException(BusinessLogicException):
    status_code = 500

    def __init__(self, message = "Unresolved error"):
        super().__init__(message)
        self.message = message


# Excepciones específicas de base de datos

class DatabaseException(Exception):
    status_code = 500

    def __init__(self, message = "Database error"):
        super().__init__(message)
        self.message = message


class SaveException(DatabaseException):
    status_code = 400

    def __init__(self, message="Error saving object to the database", *args):
        super().__init__(message, *args)
        self.message = message


class DeleteException(DatabaseException):
    status_code = 400

    def __init__(self, message="Error deleting object from the database", *args):
        super().__init__(message, *args)
        self.message = message


class UpdateException(DatabaseException):
    status_code = 400

    def __init__(self, message="Error updating object in the database", *args):
        super().__init__(message, *args)
        self.message = message

# Excepciones de autenticación

class CognitoError(Exception):
    pass

class InvalidJWTError(CognitoError):
    pass

class InvalidKidError(CognitoError):
    pass

class SignatureError(CognitoError):
    pass

class TokenExpiredError(CognitoError):
    pass

class InvalidIssuerError(CognitoError):
    pass

class InvalidAudienceError(CognitoError):
    pass

class InvalidTokenUseError(CognitoError):
    pass
