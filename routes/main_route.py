from flask import Blueprint, jsonify

# Crear un Blueprint llamado 'main'
main = Blueprint('main', __name__)

# Ruta principal
@main.route("/")
def index():
    
    # Devolver una respuesta JSON
    return jsonify(message="API is running successfully!")
