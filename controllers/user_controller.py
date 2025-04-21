# controllers/user_controller.py

from flask import make_response, request, jsonify

from services.user_service import UserService
from helpers.validate_input import validate_email
from utils.exceptions import InvalidInputException, SaveException, AlreadyExistsException, DatabaseException


"""clase para validacion de datos externos de los usuarios"""
class UserController:
   
    def __init__(self):
        self.user_service = UserService()

    # validacion de datos externos para añadir un usuario
    def add_user(self):

        email = request.json.get('email')
        group = request.json.get('group')

        # Verificar que los campos no sean nulos ni vacíos
        if not email:
            raise InvalidInputException("Se requiere un correo electrónico.")
    
        # Validar los datos de entrada
        validate_email(email)

        try:
            self.user_service.add_user(email, group)

        #TODO manejar excepciones de manera mas especifica y manejar los try/except de manera mas especifica
        except InvalidInputException as e:
            return make_response(jsonify({"error": str(e)}), 400)
        except AlreadyExistsException as e:
            return make_response(jsonify({"error": str(e)}), 409)
        except DatabaseException as e:
            return make_response(jsonify({"error": str(e)}), 500)
        except SaveException as e:
            return make_response(jsonify({"error": str(e)}), 400)
        return jsonify({"msg": "Usuario creado exitosamente"}), 200
    
    # Validacion de datos externos para iniciar sesion de un usuario
    def login_user(self):
        email = request.json.get('email')
        password = request.json.get('password')

        # Validar los datos de entrada
        if not email or not password:
            raise InvalidInputException("Correo electrónico y contraseña son requeridos.")
        
        try:
            token = self.user_service.login_user(email, password)

            return jsonify({"token": token}), 200
        
        except InvalidInputException as e:
            return make_response(jsonify({"error": str(e)}), 400)
        except Exception as e:
            return make_response(jsonify({"error": f"Error inesperado: {str(e)}"}), 500)

        
    def change_password(self):
        email = request.json.get('email')
        new_password = request.json.get('new_password')
        session = request.json.get('session')

        # Validar los datos de entrada
        if not email or not new_password or not session:
            raise InvalidInputException("Correo electrónico y nueva contraseña son requeridos.")
        
        try:
            self.user_service.change_password(email, new_password, session)

            return jsonify({"msg": "Contraseña cambiada exitosamente"}), 200
        
        except InvalidInputException as e:
            return make_response(jsonify({"error": str(e)}), 400)
        except Exception as e:
            return make_response(jsonify({"error": f"Error inesperado: {str(e)}"}), 500)


