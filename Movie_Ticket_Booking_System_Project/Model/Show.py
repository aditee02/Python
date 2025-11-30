class Show:
    def __init__(self, show_id, movie_id, hall_id, show_date, show_time):
        self.show_id = show_id
        self.movie_id = movie_id     # FK → Movie.movie_id
        self.hall_id = hall_id       # FK → Hall.hall_id
        self.show_date = show_date
        self.show_time = show_time

    def __repr__(self):
        return (f"Show(show_id={self.show_id}, movie_id={self.movie_id}, hall_id={self.hall_id}, "
                f"show_date='{self.show_date}', show_time='{self.show_time}')")
