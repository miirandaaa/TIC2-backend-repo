# models/classroom_model.py

from core.base_model import Base
from database.db import db

"""
CREATE TABLE IF NOT EXISTS public.classrooms
(
    id_classroom varchar(150) NOT NULL DEFAULT nextval('classrooms_id_classroom_seq'::regclass),
    name_classroom character varying(150) NOT NULL,
    capacity integer NOT NULL,
    min_temp numeric(10,3),
    max_temp numeric(10,3),
    min_humidity numeric(10,3),
    max_humidity numeric(10,3),
    min_co2 numeric(10,3),
    max_co2 numeric(10,3),
    CONSTRAINT classrooms_pkey PRIMARY KEY (id_classroom),
    CONSTRAINT classrooms_capacity_key UNIQUE (capacity)
)
"""

class Classroom(Base):

    __tablename__ = 'classrooms'

    id_classroom = db.Column(db.String(150), primary_key=True,)
    capacity = db.Column(db.Integer, nullable=False, unique=True)
    min_temp = db.Column(db.Numeric(10, 3))
    max_temp = db.Column(db.Numeric(10, 3))
    min_humidity = db.Column(db.Numeric(10, 3))
    max_humidity = db.Column(db.Numeric(10, 3))
    min_co2 = db.Column(db.Numeric(10, 3))
    max_co2 = db.Column(db.Numeric(10, 3))

    def __init__(self, id_classroom, capacity, min_temp=None, max_temp=None, min_humidity=None, max_humidity=None, min_co2=None, max_co2=None):
        self.id_classroom = id_classroom
        self.capacity = capacity
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.min_humidity = min_humidity
        self.max_humidity = max_humidity
        self.min_co2 = min_co2
        self.max_co2 = max_co2

    def __repr__(self):
        return f'<Classroom id_classroom={self.id_classroom}, capacity={self.capacity}>'
    
    # Metdo para obtener los datos de una clase por su id
    @classmethod
    def get_classroom_by_id_classroom(cls, id_classroom):
        return cls.query.filter_by(id_classroom=id_classroom).first()
    
    # Método para obtener todas las clases
    @classmethod
    def get_all_classrooms(cls):
        return cls.query.all()
    


