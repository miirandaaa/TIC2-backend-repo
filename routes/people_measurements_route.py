# routes/people_measurements_route.py

from flask import Blueprint, jsonify, request
from controllers.people_measurements_controller import PeopleMeasurementsController
from auth.decorators import auth_verfication

"""Este archivo define las rutas relacionadas con las mediciones de personas"""

# Blueprint para las rutas de mediciones de personas
people_measurements = Blueprint('people_measurements', __name__)

people_measurements_controller = PeopleMeasurementsController()

# Ruta para obtener todas las mediciones de personas
@people_measurements.route('/get_people_measurements', methods=['GET'])
@auth_verfication
def get_people_measurements_endpoint():
    return people_measurements_controller.get_people_measurements()

# Ruta para obtener las mediciones de personas de una clase
@people_measurements.route('/get_classroom_people_measurements', methods=['GET'])
@auth_verfication
def get_classroom_people_measurements_endpoint():
    return people_measurements_controller.get_classroom_people_measurements()

