class SeatService:
    def __init__(self, seat_dao):
        self.seat_dao = seat_dao

    def add_seat(self, hall_id, seat_number, seat_type):
        return self.seat_dao.create_seat(hall_id, seat_number, seat_type)

    def get_seats_by_hall(self, hall_id):
        return self.seat_dao.get_seats_by_hall(hall_id)

    def get_seat(self, seat_id):
        return self.seat_dao.get_seat_by_id(seat_id)
