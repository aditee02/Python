from Model.Seat import Seat
from database.connection import DatabaseConnection

class SeatDAO:
    def __init__(self, db=None):
        if db:
            self.db = db
        else:
            self.db = DatabaseConnection.get_connection()
        self.cursor = self.db.cursor()

    def create_seat(self, hall_id, seat_number, seat_type):
        query = """
        INSERT INTO seat (hall_id, seat_number, seat_type)
        VALUES (%s, %s, %s)
        """
        self.cursor.execute(query, (hall_id, seat_number, seat_type))
        self.db.commit()
        return self.cursor.lastrowid

    def get_seat_by_id(self, seat_id):
        query = "SELECT * FROM seat WHERE seat_id = %s"
        self.cursor.execute(query, (seat_id,))
        result = self.cursor.fetchone()
        if result:
            return Seat(*result)
        return None

    def get_seats_by_hall(self, hall_id):
        query = "SELECT * FROM seat WHERE hall_id = %s"
        self.cursor.execute(query, (hall_id,))
        rows = self.cursor.fetchall()
        return [Seat(*row) for row in rows]

    def get_all_seats(self):
        query = "SELECT * FROM seat"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return [Seat(*row) for row in rows]

    def close(self):
        self.cursor.close()
        self.db.close()
