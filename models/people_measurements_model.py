# model/people_measurements_model.py

from core.base_model import Base
from database.db import db

"""
CREATE TABLE IF NOT EXISTS public.people_measurements
(
    "timestamp" timestamp without time zone NOT NULL,
    count integer NOT NULL,
    id integer NOT NULL DEFAULT nextval('people_measurements_id_seq'::regclass),
    id_classroom character varying(150) COLLATE pg_catalog."default",
    CONSTRAINT people_measurements_pkey PRIMARY KEY (id)
)

"""

class PeopleMeasurements(Base):
    
    __tablename__ = 'people_measurements'

    timestamp = db.Column(db.DateTime, primary_key=True)
    count = db.Column(db.Integer, nullable=False)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_classroom = db.Column(db.String(150))

    def __init__(self, timestamp, count=None, id_classroom=None):
        self.timestamp = timestamp
        self.count = count
        self.id_classroom = id_classroom

    def __repr__(self):
        return f'<PeopleMeasurements timestamp={self.timestamp}, count={self.count}, id_classroom={self.id_classroom}>'
    
    @classmethod
    def get_people_measurements(cls):
        return cls.query.all()
    
    @classmethod
    def get_people_measurements_by_id_classroom(cls, id_classroom):
        return cls.query.filter_by(id_classroom=id_classroom).all()
    
    @classmethod
    def get_people_measurements_by_timestamp(cls, timestamp):
        return cls.query.filter_by(timestamp=timestamp).all()
    
    @classmethod
    def get_people_measurements_by_classroom_timestamp(cls, classroom, timestamp):
        return cls.query.filter_by(id_classroom=classroom, timestamp=timestamp).all()
