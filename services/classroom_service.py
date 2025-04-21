# services/classroom_service.py

from flask import jsonify, make_response
from utils.exceptions import *
from models.classroom_model import Classroom 

class ClassroomService:
    def __init__(self):
        pass

    # Metodo que obtiene todas las clases
    def get_classrooms(self):
        try:
        
            classrooms = Classroom.get_all_classrooms()

            if not classrooms:
                raise NotFoundException("No se encontraron clases.")
            
        except DatabaseException as e:
            raise DatabaseException("Error al acceder a la base de datos.")
        return classrooms
    
    # Metodo para obtener clases por su id
    def get_classroom_by_id(self, id_classroom):
        try:

            classroom = Classroom.get_classroom_by_id_classroom(id_classroom)

            if not classroom:
                raise NotFoundException("No se encontraron clases.")
       
        except DatabaseException as e:
            raise DatabaseException("Error al acceder a la base de datos.")
        return classroom