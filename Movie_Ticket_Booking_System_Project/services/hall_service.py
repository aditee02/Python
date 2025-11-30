class HallService:
    def __init__(self, hall_dao):
        self.hall_dao = hall_dao

    def add_hall(self, hall_name, cinema_id, total_seats):
        return self.hall_dao.create_hall(hall_name, cinema_id, total_seats)

    def get_halls_by_cinema(self, cinema_id):
        return self.hall_dao.get_halls_by_cinema(cinema_id)

    def get_hall(self, hall_id):
        return self.hall_dao.get_hall_by_id(hall_id)
