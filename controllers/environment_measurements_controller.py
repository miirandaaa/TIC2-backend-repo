# controllers/environment_measurements_controller.py

from flask import jsonify, make_response, request
from helpers.validate_input import validate_input
from services.environment_measurements_service import EnvironmentMeasurementsService
from utils.exceptions import *

class EnvironmentMeasurementsController:

    def __init__(self):
        self.environment_measurements_service = EnvironmentMeasurementsService()

    def get_environment_measurements(self):
        try:
            env_measurements = self.environment_measurements_service.get_environment_measurements()

            if not env_measurements:
                raise NotFoundException("No se encontraron mediciones ambientales.")
            
            env_measurements = [measurement.to_json() for measurement in env_measurements]

        except NotFoundException as e:
            return make_response(jsonify({"error": str(e)}), 404)
        except DatabaseException as e:
            return make_response(jsonify({"error": str(e)}), 500)
        return jsonify(env_measurements), 200

    def get_classroom_environment_measurements(self):

        id_classroom = request.args.get('id_classroom')

        # Validar datos externos
        if not id_classroom:
            raise InvalidInputException("Se requiere un una clase.")

        if not validate_input(id_classroom, str):
            raise InvalidInputException("El id de la clase debe ser un string.")

        try:
            env_measurements = self.environment_measurements_service.get_classroom_environment_measurements(id_classroom)

            if not env_measurements:
                raise NotFoundException("No se encontraron mediciones ambientales para la clase proporcionada.")
            
            env_measurements = [measurement.to_json() for measurement in env_measurements]

        except NotFoundException as e:
            return make_response(jsonify({"error": str(e)}), 404)
        except DatabaseException as e:
            return make_response(jsonify({"error": str(e)}), 500)
        return jsonify(env_measurements), 200
