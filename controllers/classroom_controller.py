# controllers/classroom_controller.py

from flask import jsonify, request, make_response
from services.classroom_service import ClassroomService
from utils.exceptions import *
from helpers.validate_input import validate_input

class ClassroomController:
    def __init__(self):
        self.classroom_service = ClassroomService()

    # Metodo que obtiene todas las clases
    def get_classrooms(self):
        try:
            classrooms = self.classroom_service.get_classrooms()

            if not classrooms:
                raise NotFoundException("No se encontraron clases.")
            
            classrooms = [classroom.to_json() for classroom in classrooms]
            
        except NotFoundException as e:
            return make_response(jsonify({"error": str(e)}), 404)
        except DatabaseException as e:
            return make_response(jsonify({"error": str(e)}), 500)
        except Exception as e:
            return make_response(jsonify({"error": "Error interno del servidor"}), 500)
        return jsonify(classrooms), 200
