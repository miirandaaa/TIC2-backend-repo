# modelos/user_model.py

from core.base_model import Base
from database.db import db

"""
CREATE TABLE IF NOT EXISTS public.users
(
    id_user integer NOT NULL DEFAULT nextval('users_id_user_seq'::regclass),
    cognito_sub character varying(255) COLLATE pg_catalog."default" NOT NULL,
    email character varying(255) COLLATE pg_catalog."default" NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT users_pkey PRIMARY KEY (id_user),
    CONSTRAINT users_cognito_sub_key UNIQUE (cognito_sub),
    CONSTRAINT users_email_key UNIQUE (email)
)
"""

class User(Base):
    
    __tablename__ = 'users'

    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    group = db.Column(db.String(255), nullable=True)
    

    def __init__(self, email, group):
        self.email = email
        self.group = group

    def __repr__(self):
        return f"<User {self.id_user} - {self.email}>"
    
    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    
    @classmethod
    def get_by_cognito_sub(cls, cognito_sub):
        return cls.query.filter_by(cognito_sub=cognito_sub).first()

