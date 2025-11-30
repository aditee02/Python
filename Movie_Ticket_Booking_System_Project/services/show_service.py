class ShowService:
    def __init__(self, show_dao):
        self.show_dao = show_dao

    def add_show(self, movie_id, hall_id, show_date, show_time):
        return self.show_dao.create_show(movie_id, hall_id, show_date, show_time)

    def get_shows_by_hall(self, hall_id):
        return self.show_dao.get_shows_by_hall(hall_id)

    def get_show(self, show_id):
        return self.show_dao.get_show_by_id(show_id)
