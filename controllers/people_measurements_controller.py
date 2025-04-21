# controllers/classroom_controller.py

from flask import jsonify, request
from services.people_measurements_service import PeopleMeasuremetnsService
from utils.exceptions import *


class PeopleMeasurementsController:
    def __init__(self):
        self.people_measurements_service = PeopleMeasuremetnsService()

    def get_people_measurements(self):
        try:
            people_measurements = self.people_measurements_service.get_people_measurements()

            if not people_measurements:
                raise NotFoundException("No se encontraron mediciones de personas.")

            people_measurements = [measurement.to_json() for measurement in people_measurements]

        except NotFoundException as e:
            return jsonify({"error": str(e)}), 404
        except DatabaseException as e:
            return jsonify({"error": str(e)}), 500
        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500
        return jsonify(people_measurements), 200
