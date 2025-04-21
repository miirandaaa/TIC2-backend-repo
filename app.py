# app.py
from flask import Flask
from database.db import db
from routes.main_route import main  
from routes.user_route import users
from dotenv import load_dotenv
from flask_socketio import SocketIO, send
from routes.classroom_route import classroom
from routes.environment_measurements_route import environment_measurements
from routes.people_measurements_route import people_measurements
import os

# Cargar variables de entorno desde .env
load_dotenv()

# Obtener las variables de entorno
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

app = Flask(__name__)

# Configuración de conexión a la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la app con la base de datos
db.init_app(app)


# Registrar los Blueprint de las rutas
app.register_blueprint(main)
app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(classroom, url_prefix='/classroom')
app.register_blueprint(environment_measurements, url_prefix='/environment_measurements')
app.register_blueprint(people_measurements, url_prefix='/people_measurements')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
