# routes/classroom_route.py

from flask import Blueprint, jsonify, request
from controllers.classroom_controller import ClassroomController
from auth.decorators import auth_verfication

"""Este archivo define las rutas relacionadas con las clases"""   

# Blueprint para las rutas de clase
classroom = Blueprint('classroom', __name__)

classroom_controller = ClassroomController()

# Ruta para acceder a todas las clases 
@classroom.route('/get_classrooms', methods=['GET'])
@auth_verfication
def get_classrooms_endpoint():
    return classroom_controller.get_classrooms()

