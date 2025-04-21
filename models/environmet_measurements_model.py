# model/environmet_measurements_model.py

from core.base_model import Base
from database.db import db

"""
CREATE TABLE IF NOT EXISTS public.enviroment_measurements
(
    "timestamp" timestamp without time zone NOT NULL,
    temperature numeric(10,3),
    humidity numeric(10,3),
    co2 numeric(10,3),
    id integer NOT NULL DEFAULT nextval('air_measurements_id_seq'::regclass),
    id_classroom character varying(150) COLLATE pg_catalog."default",
    CONSTRAINT air_measurements_pkey PRIMARY KEY (id)
)
"""

class EnvironmentMeasurements(Base):

    __tablename__ = 'environment_measurements'

    timestamp = db.Column(db.DateTime, primary_key=True)
    temperature = db.Column(db.Numeric(10, 3))
    humidity = db.Column(db.Numeric(10, 3))
    co2 = db.Column(db.Numeric(10, 3))
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_classroom = db.Column(db.String(150))

    def __init__(self, timestamp, temperature=None, humidity=None, co2=None, id_classroom=None):
        self.timestamp = timestamp
        self.temperature = temperature
        self.humidity = humidity
        self.co2 = co2
        self.id_classroom = id_classroom

    def __repr__(self):
        return f'<EnvironmentMeasurements timestamp={self.timestamp}, temperature={self.temperature}, humidity={self.humidity}, co2={self.co2}, id_classroom={self.id_classroom}>'
    
    @classmethod
    def get_environmet_measurements(cls):
        return cls.query.all()
    
    @classmethod
    def get_classroom_enviroment_measurements(cls, id_classroom):
        return cls.query.filter_by(id_classroom=id_classroom).all()
    
    @classmethod
    def get_enviroment_measurements_by_timestamp(cls, timestamp):
        return cls.query.filter_by(timestamp=timestamp).all()
    
    @classmethod 
    def get_enviroment_measurements_by_classroom_timestamp(cls, id_classroom, timestamp):
        return cls.query.filter_by(id_classroom=id_classroom, timestamp=timestamp).all()
    