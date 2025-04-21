# services/environment_measurements_service.py

from flask import jsonify, make_response
from models.environmet_measurements_model import EnvironmentMeasurements
from utils.exceptions import *

class EnvironmentMeasurementsService:

    def __init__(self):
        pass

    def get_environment_measurements(self):
        try:
            env_measurements = EnvironmentMeasurements.get_environmet_measurements()

            if not env_measurements:
                raise NotFoundException("No se encontraron mediciones ambientales.")
            
        except DatabaseException as e:
            raise DatabaseException("Error al acceder a la base de datos.")
        return env_measurements