class Movie:
    def __init__(self, movie_id, title, genre, language, duration, extra=None):
        self.movie_id = movie_id
        self.title = title
        self.genre = genre
        self.language = language
        self.duration = duration
        self.extra = extra  # optional column

    def __repr__(self):
        return f"Movie(movie_id={self.movie_id}, title='{self.title}', genre='{self.genre}', language='{self.language}', duration={self.duration})"
