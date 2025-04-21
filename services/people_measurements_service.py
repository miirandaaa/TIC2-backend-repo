# services/people_measurements_service.py

from flask import jsonify, make_response, request
from helpers.validate_input import validate_input
from utils.exceptions import *
from models.people_measurements_model import PeopleMeasurements


class PeopleMeasuremetnsService:
    def __init__(self):
        pass

    def get_people_measurements(self):
        try:   

            people_measurements = PeopleMeasurements.get_people_measurements()

            if not people_measurements:
                raise NotFoundException("No se encontraron mediciones de personas.")

        except NotFoundException as e:
            raise NotFoundException("No se encontraron mediciones de personas.")
        except DatabaseException as e:
            raise DatabaseException("Error al acceder a la base de datos.")
        return people_measurements

    def get_classroom_people_measurements(self, id_classroom):
        pass