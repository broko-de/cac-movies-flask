from app.database import db

class Movie(db.Model):
    __tablename__ = 'movies'

    id_movie = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    director = db.Column(db.String(255), nullable=False)
    release_date = db.Column(db.Date)
    banner = db.Column(db.String(255))

    def __init__(self, title, director, release_date, banner):
        self.title = title
        self.director = director
        self.release_date = release_date
        self.banner = banner
    
    def serialize(self):
        return {
            'id_movie': self.id_movie,
            'title': self.title,
            'director': self.director,
            'release_date': str(self.release_date),  # Convertir la fecha a una cadena para la serialización JSON
            'banner': self.banner
        }