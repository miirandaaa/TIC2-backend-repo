# core/base_model.py

from sqlalchemy.orm import DeclarativeBase
from database.db import db
from datetime import datetime, date, time
from decimal import Decimal
from sqlalchemy import select
from utils.exceptions import SaveException, DeleteException, UpdateException

class AuxiliarMixin:
    def to_json(self):
        result = {}
        for c in self.__table__.columns:
            value = getattr(self, c.key)
            if isinstance(value, (datetime, date, time)):
                result[c.key] = value.isoformat()
            else:
                result[c.key] = value
        return result

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise SaveException(f'ERROR: Could not save object {self.__class__.__name__}!') from e
        return self


    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise DeleteException(f'ERROR: Could not delete object {self.__class__.__name__}!') from e
        return self

    def update(self):
        try:
            db.session.merge(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise UpdateException(f'ERROR: Could not update object {self.__class__.__name__}!') from e
        return self

""" Defino una clase base para los modelos de la base de datos:
    Esta clase hereda de db.Model y AuxiliarMixin.
    db.Model es la clase base de SQLAlchemy para definir modelos de base de datos
    AuxiliarMixin es una clase que contiene métodos auxiliares para manejar operaciones comunes
    como guardar, eliminar y actualizar objetos en la base de datos.
"""
class Base(db.Model, AuxiliarMixin):
    __abstract__ = True
