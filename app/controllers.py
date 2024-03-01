from flask import jsonify, request
from app.database import db
from app.models import Movie

def create_movie():
    data = request.json
    new_movie = Movie(**data)
    db.session.add(new_movie)
    db.session.commit()
    return jsonify({'message': 'Movie created successfully'}), 201

def get_all_movies():
    movies = Movie.query.all()
    return jsonify([movie.serialize() for movie in movies])

def get_movie(movie_id):
    movie = Movie.query.get(movie_id)
    if not movie:
        return jsonify({'message': 'Movie not found'}), 404
    return jsonify(movie.serialize())

def update_movie(movie_id):
    movie = Movie.query.get(movie_id)
    if not movie:
        return jsonify({'message': 'Movie not found'}), 404
    data = request.json
    movie.title = data.get('title', movie.title)
    movie.director = data.get('director', movie.director)
    movie.release_date = data.get('release_date', movie.release_date)
    movie.banner = data.get('banner', movie.banner)
    db.session.commit()
    return jsonify({'message': 'Movie updated successfully'})

def delete_movie(movie_id):
    movie = Movie.query.get(movie_id)
    if not movie:
        return jsonify({'message': 'Movie not found'}), 404
    db.session.delete(movie)
    db.session.commit()
    return jsonify({'message': 'Movie deleted successfully'})