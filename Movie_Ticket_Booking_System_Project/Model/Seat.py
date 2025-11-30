class Seat:
    def __init__(self, seat_no, hall_name, reserved=False):
        self.seat_no = seat_no
        self.hall_name = hall_name
        self.reserved = reserved

    def __repr__(self):
        return f"Seat(seat_no={self.seat_no}, hall_name='{self.hall_name}', reserved={self.reserved})"
