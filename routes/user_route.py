# routes/user_route.py

from flask import Blueprint, jsonify, request
from controllers.user_controller import UserController

"""Este archivo define las rutas relacionadas con los usuarios"""

# Blueprint para las rutas de usuario
users = Blueprint('users', __name__)

user_controller = UserController()


# Ruta para registrar un nuevo usuario
@users.route('/add_user', methods=['POST'])
def add_user_endpoint():
    return user_controller.add_user()

# Ruta para iniciar sesión de un usuario
@users.route('/login', methods=['POST'])
def login_endpoint():
    return user_controller.login_user()

# Ruta para cambiar contrasena
@users.route('/change_password', methods=['POST'])
def change_password_endpoint():
    return user_controller.change_password()