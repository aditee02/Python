class BookingService:
    def __init__(self, booking_dao, seat_dao):
        self.booking_dao = booking_dao
        self.seat_dao = seat_dao

    def create_booking(self, user_id, show_id, seat_id, booking_time, amount):
        seat = self.seat_dao.get_seat_by_id(seat_id)

        if seat is None:
            raise Exception("Seat does not exist")

        if self.booking_dao.is_seat_booked(show_id, seat_id):
            raise Exception("Seat already booked")

        return self.booking_dao.create_booking(
            user_id, show_id, seat_id, booking_time, amount
        )

    def get_bookings_by_user(self, user_id):
        return self.booking_dao.get_bookings_by_user(user_id)

    def list_all_bookings(self):
        return self.booking_dao.get_all_bookings()
