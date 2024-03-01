import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Crear una instancia de SQLAlchemy
db = SQLAlchemy()

def init_db(app):
    # Configurar la URI de la base de datos desde las variables de entorno
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

    # Configurar el seguimiento de modificaciones en la base de datos
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar la base de datos con la aplicación Flask
    db.init_app(app)