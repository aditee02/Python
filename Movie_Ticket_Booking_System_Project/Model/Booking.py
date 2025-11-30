class Booking:
    def __init__(self, booking_id, user_id, show_id, seat_id, booking_time, price):
        self.booking_id = booking_id
        self.user_id = user_id
        self.show_id = show_id
        self.seat_id = seat_id
        self.booking_time = booking_time
        self.price = price

    def __repr__(self):
        return f"Booking(booking_id={self.booking_id}, user_id={self.user_id}, show_id={self.show_id}, seat_id={self.seat_id}, booking_time='{self.booking_time}', price={self.price})"
