from flask import Flask
from app.database import init_app
from app.controllers import *

app = Flask(__name__)

# Configurar la aplicación Flask
# app.config.from_pyfile('config/development.py')

# Inicializar la base de datos con la aplicación Flask
init_app(app)

# Rutas para el CRUD de la entidad Movie
app.route('/api/movies/', methods=['POST'])(create_movie)
app.route('/api/movies/', methods=['GET'])(get_all_movies)
app.route('/api/movies/<int:movie_id>', methods=['GET'])(get_movie)
app.route('/api/movies/<int:movie_id>', methods=['PUT'])(update_movie)
app.route('/api/movies/<int:movie_id>', methods=['DELETE'])(delete_movie)

if __name__ == '__main__':
    app.run(debug=True)