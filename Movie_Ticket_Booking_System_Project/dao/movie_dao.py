from Model.Movie import Movie
from database.connection import DatabaseConnection

class MovieDAO:
    def __init__(self, db=None):
        self.db = db or DatabaseConnection.get_connection()
        self.cursor = self.db.cursor()

    def create_movie(self, title, genre, language, duration):
        query = """
        INSERT INTO movie (title, genre, language, duration)
        VALUES (%s, %s, %s, %s)
        """
        self.cursor.execute(query, (title, genre, language, duration))
        self.db.commit()
        return self.cursor.lastrowid

    def get_movie_by_id(self, movie_id):
        query = "SELECT movie_id, title, genre, language, duration FROM movie WHERE movie_id = %s"
        self.cursor.execute(query, (movie_id,))
        res = self.cursor.fetchone()
        if res:
            return Movie(*res)
        return None

    def get_all_movies(self):
        query = "SELECT movie_id, title, genre, language, duration FROM movie"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return [Movie(*row) for row in rows]

    def close(self):
        self.cursor.close()
        self.db.close()
