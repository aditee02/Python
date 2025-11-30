class Hall:
    def __init__(self, hall_id, cinema_id, hall_number):
        self.hall_id = hall_id
        self.cinema_id = cinema_id
        self.hall_number = hall_number

    def __repr__(self):
        return f"Hall(hall_id={self.hall_id}, cinema_id={self.cinema_id}, hall_number={self.hall_number})"
