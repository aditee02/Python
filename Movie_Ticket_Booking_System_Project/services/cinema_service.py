class CinemaService:
    def __init__(self, cinema_dao):
        self.cinema_dao = cinema_dao

    def add_cinema(self, cinema_name, city_id):
        return self.cinema_dao.create_cinema(cinema_name, city_id)

    def get_cinemas_by_city(self, city_id):
        return self.cinema_dao.get_cinemas_by_city(city_id)

    def get_cinema(self, cinema_id):
        return self.cinema_dao.get_cinema_by_id(cinema_id)
