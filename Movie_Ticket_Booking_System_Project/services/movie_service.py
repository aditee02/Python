class MovieService:
    def __init__(self, movie_dao):
        self.movie_dao = movie_dao

    def add_movie(self, title, genre, language, duration_min, rating):
        return self.movie_dao.create_movie(title, genre, language, duration_min, rating)

    def list_movies(self):
        return self.movie_dao.get_all_movies()

    def get_movie(self, movie_id):
        return self.movie_dao.get_movie_by_id(movie_id)
