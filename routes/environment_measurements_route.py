# routes/environment_measurements_route.py

from flask import Blueprint
from controllers.environment_measurements_controller import EnvironmentMeasurementsController
from auth.decorators import auth_verfication

"""Este archivo define las rutas relacionadas con las mediciones ambientales"""

# Blueprint para las rutas de mediciones ambientales
environment_measurements = Blueprint('environment_measurements', __name__)

environment_measurements_controller = EnvironmentMeasurementsController()


# Ruta para obtener todas las mediciones ambientales
@environment_measurements.route('/get_environment_measurements', methods=['GET'])
@auth_verfication
def get_environment_measurements_endpoint():
    return environment_measurements_controller.get_environment_measurements()

# Ruta para obtener las mediciones ambientales de una clase
@environment_measurements.route('/get_classroom_environment_measurements', methods=['GET'])
@auth_verfication
def get_classroom_environment_measurements_endpoint():
    return environment_measurements_controller.get_classroom_environment_measurements()

# Ruta para obtener las mediciones ambientales en tiempo
@environment_measurements.route('/get_environment_measurements_by_timestamp', methods=['GET'])
@auth_verfication
def get_environment_measurements_by_timestamp_endpoint():
    return environment_measurements_controller.get_environment_measurements_by_timestamp()
